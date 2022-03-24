-- Limpeza dos dados usando Queries

SELECT * 
FROM [Nashville Housing Project].dbo.NashvilleHousing

-- Padronização das datas

SELECT SaleDateConverted, CONVERT(Date, SaleDate) 
FROM [Nashville Housing Project].dbo.NashvilleHousing

UPDATE NashvilleHousing
SET SaleDate = CONVERT(Date, SaleDate)

ALTER TABLE NashvilleHousing
Add SaleDateConverted Date;

UPDATE NashvilleHousing
SET SaleDateConverted = CONVERT(Date, SaleDate)

-- Populando os dados de endereço da propriedade

SELECT *
FROM [Nashville Housing Project].dbo.NashvilleHousing
--WHERE PropertyAddress is null
ORDER BY ParcelID


SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Nashville Housing Project].dbo.NashvilleHousing a
JOIN [Nashville Housing Project].dbo.NashvilleHousing b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress is null

UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Nashville Housing Project].dbo.NashvilleHousing a
JOIN [Nashville Housing Project].dbo.NashvilleHousing b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress is null


-- Separando os endereços por valores individuais (Endereço, Cidade, Estado)

SELECT PropertyAddress
FROM [Nashville Housing Project].dbo.NashvilleHousing
--WHERE PropertyAddress is null
--ORDER BY ParcelID

SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',',PropertyAddress)-1) as Address
, SUBSTRING(PropertyAddress, CHARINDEX(',',PropertyAddress)+1, LEN(PropertyAddress)) as Address

FROM [Nashville Housing Project].dbo.NashvilleHousing

ALTER TABLE NashvilleHousing
Add PropertySplitAddress NVARCHAR(255);

UPDATE NashvilleHousing
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',',PropertyAddress)-1)

ALTER TABLE NashvilleHousing
Add PropertySplitCity NVARCHAR(255);

UPDATE NashvilleHousing
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',',PropertyAddress)+1, LEN(PropertyAddress))



SELECT *
FROM [Nashville Housing Project].dbo.NashvilleHousing





SELECT OwnerAddress
FROM [Nashville Housing Project].dbo.NashvilleHousing

SELECT 
PARSENAME(REPLACE(OwnerAddress,',', '.'),  3),
PARSENAME(REPLACE(OwnerAddress,',', '.'),  2),
PARSENAME(REPLACE(OwnerAddress,',', '.'),  1)
FROM [Nashville Housing Project].dbo.NashvilleHousing

ALTER TABLE NashvilleHousing
Add OwnerSplitAddress NVARCHAR(255);

UPDATE NashvilleHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress,',', '.'),  3)

ALTER TABLE NashvilleHousing
Add OwnerSplitCity NVARCHAR(255);

UPDATE NashvilleHousing
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress,',', '.'),  2)

ALTER TABLE NashvilleHousing
Add OwnerSplitState NVARCHAR(255);

UPDATE NashvilleHousing
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress,',', '.'),  1)

SELECT *
FROM [Nashville Housing Project].dbo.NashvilleHousing

-- Mudando Y e N para Yes e No na coluna "Sold as Vacant"

SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant) 
FROM [Nashville Housing Project].dbo.NashvilleHousing
GROUP BY SoldAsVacant
ORDER BY 2



SELECT SoldAsVacant,
CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	 WHEN SoldAsVacant = 'N' THEN 'No'
	 ELSE SoldAsVacant
	 END
FROM [Nashville Housing Project].dbo.NashvilleHousing


UPDATE NashvilleHousing
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	 WHEN SoldAsVacant = 'N' THEN 'No'
	 ELSE SoldAsVacant
	 END

-- Removendo registros duplicados

WITH RowNumCTE as(
SELECT *,
	ROW_NUMBER() OVER(
	PARTITION BY ParcelID,
				 PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY
					UniqueID
					) row_num
FROM [Nashville Housing Project].dbo.NashvilleHousing
--order by ParcelID
)
SELECT * 
FROM RowNumCTE
WHERE row_num  > 1
ORDER BY PropertyAddress


--Deletando Colunas não usadas


SELECT *
FROM [Nashville Housing Project].dbo.NashvilleHousing


ALTER TABLE [Nashville Housing Project].dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress

ALTER TABLE [Nashville Housing Project].dbo.NashvilleHousing
DROP COLUMN SaleDate
