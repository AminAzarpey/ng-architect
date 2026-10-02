import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";

const projectRoot = new URL("../", import.meta.url);
const localEnvironment = new URL(".env.local", projectRoot);
if (existsSync(localEnvironment)) {
  process.loadEnvFile(fileURLToPath(localEnvironment));
}

const args = process.argv.slice(2);
const license = process.env.PRIMEUI_LICENSE_KEY?.trim();
if (license) {
  args.push("--define", `PRIMEUI_LICENSE_KEY=${JSON.stringify(license)}`);
}

const cli = new URL("node_modules/@angular/cli/bin/ng.js", projectRoot);
const child = spawn(process.execPath, [fileURLToPath(cli), ...args], {
  cwd: fileURLToPath(projectRoot),
  stdio: "inherit",
});

child.on("error", () => {
  console.error("Unable to start Angular CLI. Run mise run install first.");
  process.exitCode = 1;
});
child.on("exit", (code, signal) => {
  if (signal) {
    process.kill(process.pid, signal);
  } else {
    process.exitCode = code ?? 1;
  }
});
