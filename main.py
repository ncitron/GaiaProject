import math;
from astroquery.gaia import Gaia;
from astropy import units as u;
from astropy.coordinates import SkyCoord;

def getTables():
    tables = Gaia.load_tables(only_names=True);
    result = [];
    for table in tables:
        result.append(table.get_qualified_name());
    return result;
#Change More change

def tester():
    query = "select count(*) as numEntries from gaiadr2.gaia_source where bp_rp > 1.5";
    job = Gaia.launch_job_async(query);
    print(job.get_results());


def findObj(coord):
    job = Gaia.cone_search_async(coord, u.Quantity(.01, u.deg));
    result = job.get_results();
    result = result['source_id'];
    return result[0];


def getDist(sid):
    job = Gaia.launch_job("select * from gaiadr2.gaia_source where source_id = " + str(sid));
    obj = job.get_results();
    parallax = obj['parallax'];
    parallax = parallax[0];
    dist = (1/(parallax/1000))*3.26156;
    return dist;


def getTemp(sid):
        job = Gaia.launch_job("select * from gaiadr2.gaia_source where source_id = " + str(sid));
        obj = job.get_results();
        bp_rp = obj['bp_rp'];
        bp_rp = bp_rp[0];
        b_v = (32875-math.sqrt(1077605530-275750000*bp_rp))/5515;
        temp = 8540/(b_v+0.865);
        return temp;


def getRadius(sid):
    job = Gaia.launch_job("select * from gaiadr2.gaia_source where source_id = " + str(sid));
    obj = job.get_results();
    gmag = obj['phot_g_mean_mag'];
    gmag = gmag[0];
    absmag = gmag - 5 * math.log10(getDist(sid)/3.26156)+5;
    r = (5800/getTemp(sid))**2 * (2.512**(4.68-absmag))**(1/2);     #need to find a better fit for the magnitude of sun in Gaia G band
    return r;


def star(ra, dec):
    stats = []
    coord=SkyCoord(ra, dec);
    stats.append(getDist(findObj(coord)));
    stats.append(getTemp(findObj(coord)));
    stats.append(getRadius(findObj(coord)));
    print(stats)
    return stats;

#print(*getTables(), sep = '\n');
#tester();
