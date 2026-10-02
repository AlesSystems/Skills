import { execFileSync } from "node:child_process";
import type { FrontierPr } from "./store.ts";

type Query = (pr: number) => unknown;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

export function githubFrontier(repo: string, prs: readonly number[], query?: Query): readonly FrontierPr[] {
  if (prs.length === 0 || prs.some(pr => !Number.isSafeInteger(pr) || pr < 1) || new Set(prs).size !== prs.length) {
    throw new Error("GitHub frontier requires unique positive PR numbers in bottom-to-top order");
  }
  const fetch = query ?? ((pr: number): unknown => JSON.parse(execFileSync("gh", [
    "pr", "view", String(pr), "--json", "number,headRefName,baseRefName,headRefOid,state",
  ], { cwd: repo, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] })));
  let previous: FrontierPr | undefined;
  return prs.map(pr => {
    const raw = fetch(pr);
    if (!isRecord(raw) || raw.number !== pr || typeof raw.headRefName !== "string" || !raw.headRefName ||
      typeof raw.baseRefName !== "string" || !raw.baseRefName || typeof raw.headRefOid !== "string" ||
      !/^[0-9a-f]{40,64}$/i.test(raw.headRefOid) || (raw.state !== "OPEN" && raw.state !== "MERGED" && raw.state !== "CLOSED")) {
      throw new Error(`Invalid GitHub frontier data for PR ${pr}`);
    }
    if (raw.state === "CLOSED") throw new Error(`PR ${pr} is closed without merge; reconcile the stack before advancing`);
    if (previous?.state === "OPEN" && (raw.baseRefName !== previous.branches || raw.state === "MERGED")) {
      throw new Error(`PR ${pr} does not follow open PR ${previous.pr}; reconcile bottom-to-top stack order`);
    }
    const row: FrontierPr = { pr, branches: raw.headRefName, sha: raw.headRefOid, state: raw.state };
    previous = row;
    return row;
  });
}
