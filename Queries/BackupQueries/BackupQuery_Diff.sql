BACKUP DATABASE [HouseRentalDB]
   To DISK='D:\Database 2\Backups\HouseRentalDB_Diff.BAK'
   WITH DIFFERENTIAL,
      MEDIANAME = 'Native_SQLServerDiffBackup',
      NAME = 'Diff-HouseRentalDB backup';