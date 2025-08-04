# Sensitive Data Redacted in Azure Data Factory Pipeline JSONs

This document serves as a note that sensitive information in the Azure Data Factory pipeline JSONs has been redacted for security purposes.

## Redacted Information:

- **Dataset References**: Certain dataset references in the pipelines have been redacted to ensure sensitive paths and dataset names are not exposed.
- **File Paths**: Paths to data containers and files are redacted to avoid revealing sensitive storage locations.
- **Environment-Specific Information**: Any references or values that are specific to the environment, such as linked services or private keys, have been removed.

## Purpose:

The redactions ensure that sensitive data, including storage details, table names, and data structures, are kept secure during sharing or showcasing of the pipeline configurations.
