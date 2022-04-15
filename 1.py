from django.contrib.gis.geoip2 import GeoIP2

g = GeoIP2('geoip')
print(g)
g.country('google.com')
