import { describe, expect, it } from "bun:test";
import { githubFrontier } from "./github-frontier.ts";

const sha = "a".repeat(40);
const row = (number: number, headRefName: string, baseRefName: string, state = "OPEN") => ({ number, headRefName, baseRefName, headRefOid: sha, state });

describe("GitHub frontier", () => {
  it("keeps the supplied stack order and GitHub head SHAs", () => {
    const records = [row(12, "first", "main"), row(13, "second", "first")];
    expect(githubFrontier("unused", [12, 13], pr => records.find(r => r.number === pr))).toEqual([
      { pr: 12, branches: "first", sha, state: "OPEN" }, { pr: 13, branches: "second", sha, state: "OPEN" },
    ]);
  });
  it("allows a child retargeted to trunk after its parent merged", () => {
    const records = [row(12, "first", "main", "MERGED"), row(13, "second", "main")];
    expect(githubFrontier("unused", [12, 13], pr => records.find(r => r.number === pr))[1].pr).toBe(13);
  });
  it("rejects independent PRs masquerading as a stack", () => {
    expect(() => githubFrontier("unused", [12, 13], pr => row(pr, String(pr), "main"))).toThrow("does not follow");
  });
  it("rejects a merged child above an open parent", () => {
    expect(() => githubFrontier("unused", [12, 13], pr => row(pr, String(pr), pr === 13 ? "12" : "main", pr === 13 ? "MERGED" : "OPEN"))).toThrow("does not follow");
  });
  it("rejects closed-unmerged entries before reporting completion", () => {
    expect(() => githubFrontier("unused", [12], pr => row(pr, "first", "main", "CLOSED"))).toThrow("closed without merge");
  });
  it("rejects missing, duplicate, and malformed inputs", () => {
    expect(() => githubFrontier("unused", [], () => null)).toThrow();
    expect(() => githubFrontier("unused", [12, 12], () => null)).toThrow();
    expect(() => githubFrontier("unused", [12], () => ({ ...row(12, "first", "main"), headRefOid: "bad" }))).toThrow();
    expect(() => githubFrontier("unused", [12], () => row(13, "first", "main"))).toThrow();
  });
});
