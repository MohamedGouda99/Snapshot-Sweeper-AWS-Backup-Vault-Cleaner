# AWS Backup Vault Cleanup Script

This Python script automates the cleanup of AWS Backup Vault, allowing for efficient management of snapshots. It identifies and deletes recovery points older than a specified threshold.

## Features

- Customizable cleanup window (from 7 to 30 days).
- Seamless integration with AWS services through Boto3.
- Detailed logging for easy monitoring.

## Usage

1. Ensure you have Python and Boto3 installed.
2. Set `backup_vault_name` variable to your desired Backup Vault.
3. Run the script to initiate cleanup.

```bash
python cleanup_script.py