BACKUP DATABASE [HouseRentalDB]
	To DISK='D:\Database 2\Backups\HouseRentalDB.BAK'
	MIRROR TO DISK =  'D:\Database 2\Backups\HouseRentalDB_2.BAK'
	WITH FORMAT,
      MEDIANAME = 'Native_SQLServerBackup',
      NAME = 'Full-HouseRentalDB backup';


BACKUP DATABASE [HouseRentalDB]
   To DISK='D:\Database 2\Backups\HouseRentalDB_Diff.BAK'
   WITH DIFFERENTIAL,
      MEDIANAME = 'Native_SQLServerDiffBackup',
      NAME = 'Diff-HouseRentalDB backup';

BACKUP LOG [HouseRentalDB]
   To DISK='D:\Database 2\Backups\HouseRentalDB_Log.trn'
   WITH
   MEDIANAME = 'Native_SQLServerLogBackup',
    NAME = 'Log-HouseRentalDB backup';