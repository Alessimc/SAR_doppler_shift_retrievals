import xarray as xr

file = 'https://thredds.met.no/thredds/dodsC/remotesensingenvisat/asar-doppler/2012/03/13/ASA_WSDV2PRNMI20120313_213710_000624793112_00331_52500_0000.nc'

xrds = xr.open_dataset(file)

print(xrds)