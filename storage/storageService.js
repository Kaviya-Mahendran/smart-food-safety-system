// storage/storageService.js
import fs from "fs";
import path from "path";

const BASE_PATH = path.resolve(process.cwd(), "storage", "data");

/**
 * Ensure directory exists
 */
function ensureDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

/**
 * Read JSON safely
 */
function readJSON(filePath) {
  if (!fs.existsSync(filePath)) return null;
  const raw = fs.readFileSync(filePath, "utf-8");
  return JSON.parse(raw);
}

/**
 * Write JSON safely
 */
function writeJSON(filePath, data) {
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
}

/**
 * Public API
 */
export const StorageService = {
  read(namespace, key) {
    const filePath = path.join(BASE_PATH, namespace, `${key}.json`);
    return readJSON(filePath);
  },

  write(namespace, key, data) {
    const filePath = path.join(BASE_PATH, namespace, `${key}.json`);
    writeJSON(filePath, data);
    return { status: "saved", path: filePath };
  },

  delete(namespace, key) {
    const filePath = path.join(BASE_PATH, namespace, `${key}.json`);
    if (fs.existsSync(filePath)) {
      fs.unlinkSync(filePath);
      return { status: "deleted" };
    }
    return { status: "not_found" };
  }
};
