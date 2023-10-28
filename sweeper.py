import boto3
from datetime import datetime, timedelta

backup_vault_name = 'Default'
session = boto3.session.Session()
backup_client = session.client('backup')

for days_ago in range(7, 31):
    target_date = datetime.now() - timedelta(days=days_ago)

    response = backup_client.list_recovery_points_by_backup_vault(
        BackupVaultName=backup_vault_name,
        ByCreatedBefore=target_date
    )

    recovery_points = response['RecoveryPoints']

    if recovery_points:
        print(f"Deleting recovery points older than {days_ago} days...")

        for recovery_point in recovery_points:
            recovery_point_arn = recovery_point['RecoveryPointArn']
            print(f"Deleting recovery point: {recovery_point_arn}")
            try:
                backup_client.delete_recovery_point(
                    BackupVaultName=backup_vault_name,
                    RecoveryPointArn=recovery_point_arn
                )
                print(f"Deletion completed for {recovery_point_arn}")
            except Exception as e:
                print(f"Error occurred while deleting {recovery_point_arn}: {e}")
        print(f"Deletion completed for snapshots older than {days_ago} days.")
    else:
        print(f"No snapshots found older than {days_ago} days.")