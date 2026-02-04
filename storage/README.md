## Storage Layer

This folder provides a lightweight persistence layer shared across the system.

### Purpose
- Centralise all read/write operations
- Keep business logic out of filesystem concerns
- Allow future migration to databases or cloud storage without refactoring core logic

### Design
- `storageService.js` is the core abstraction
- Feature-specific files (scan, freshness) expose small, intentional APIs
- Data is namespaced to avoid cross-module coupling

### Current Implementation
- Local JSON storage (file-based)
- Designed for prototyping and model validation

### Future Extensions
- Replace filesystem with:
  - PostgreSQL
  - Firestore
  - S3 / Blob storage
- Add versioning and audit trails if required
