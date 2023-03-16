#Quote Name : CNX RESOURCES_DB_NAM_MSA_Canada_This is my sample python programming to get quote name
customer = "CNX RESOURCES / UNITED STATES"
primaryTier3 = "Drill Bits"
region = "North America"
subRegion = "N Amer - Land - Canada"
contractType = "Master Service Agreement"
SampleText = "This is my sample python programming to get quote name"\

a = customer.split(' / ')
aa = a[0]
b = primaryTier3.replace("Drill Bits", "DB_")
c = region.replace("North America", "NAM_")
d = subRegion.split("-")
e = d[2] + ' _ '
ee = e.replace(' ','')
f = contractType.replace("Master Service Agreement", "MSA_")
result = aa+b+c+ee+f+ SampleText
print(result[0:80])

