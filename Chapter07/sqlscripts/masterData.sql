CREATE TABLE dbo.Dim_VehicleMaster
(
Id INT IDENTITY(1,1) NOT NULL,
VehicleId VARCHAR(100) NOT NULL,
Make VARCHAR(50) NOT NULL,
Model VARCHAR(50) NOT NULL,
Category VARCHAR(200) NOT NULL,
ModelYear INT NOT NULL
)
WITH
(
    DISTRIBUTION = HASH (VehicleId),
    CLUSTERED COLUMNSTORE INDEX
)
GO

INSERT INTO dbo.Dim_VehicleMaster(VehicleId,Make,Model,Category,ModelYear)
SELECT '4b1e829f-5f32-4ae9-b415-9e7f0eb15401', 'BMW','1 Series', 'Coupe, Convertible',2013
UNION
SELECT '115e6d02-4a43-4131-b6af-9d2a8d642073', 'BMW','M Series', 'Convertible',2013
UNION
SELECT '90ccea91-416e-453f-b582-e6f04f02ee40', 'Toyota','2500 Crew Cab','Pickup',2021
UNION 
SELECT 'aa7e09d0-92cb-4cc0-99e2-04602ab0f85a','Chevrolet','2500 Extended Cab','Pickup',1992
UNION
SELECT 'b51480fc-af07-491d-b914-fec46d7d7d47','Chevrolet','300 CE','Coupe',1992
UNION
SELECT '5cb4ae8e-19de-40e1-96b5-874ffc43210b', 'Saab','3-Sep','Hatchback, Convertible',1999
UNION
SELECT 'c79935cc-0b88-44ae-9765-a68d3c0fd37d', 'Chrysler','300','Sedan',2017
UNION 
SELECT '04ac43cf-ed3c-4fb7-a15e-2dabd3c8342e', 'Mitsubishi','3000GT','Hatchback',1999
UNION
SELECT '2832b3ec-222c-4049-9af5-45a8d66d6b58', 'MAZDA','323','Hatchback',1992
UNION
SELECT '288e3ee8-ea29-489b-9c3d-07e7c6d6ee99','Toyota','4Runner','SUV',2013
GO
SELECT * FROM dbo.Dim_VehicleMaster
GO


CREATE TABLE dbo.Dim_Location
(
  LocationId INT IDENTITY(1,1) NOT NULL,
  Borough VARCHAR(20) NOT NULL,
  Location VARCHAR(100) NOT NULL,
  Latitude VARCHAR(20) NOT NULL , 
  Longitude VARCHAR(20) NOT NULL
)
WITH
(
    DISTRIBUTION = HASH (Borough),
    CLUSTERED COLUMNSTORE INDEX
)
GO
INSERT INTO dbo.Dim_Location (Borough,Location,Latitude,Longitude)
SELECT 'MANHATTAN','339 East 12th Street','40.73061','-73.984016'
UNION
SELECT 'BROOKLYN','185 Erasmus Street','40.650002', '-73.949997'
UNION
SELECT 'STATEN ISLAND','630 Richmond Hill Road','40.579021', '-74.151535'
UNION
SELECT 'BRONX','1475 Thieriot Avenue','40.837048', '-73.865433'
UNION
SELECT 'QUEENS','Thrilla, New York','40.742054', '-73.769417'
SELECT * FROM dbo.Dim_Location
GO
