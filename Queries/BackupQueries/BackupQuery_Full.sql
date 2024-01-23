BACKUP DATABASE [HouseRentalDB]
	To DISK='D:\Database 2\Backups\HouseRentalDB.BAK'
	MIRROR TO DISK =  'D:\Database 2\Backups\HouseRentalDB_2.BAK'
	WITH FORMAT,
      MEDIANAME = 'Native_SQLServerBackup',
      NAME = 'Full-HouseRentalDB backup';
