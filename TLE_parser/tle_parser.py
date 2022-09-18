import math as m

lines = []
#Reference to obtain eccentric anomaly and semi-major axis
#https://blog.hardinglabs.com/tle-to-kep.html 

with open('TLE.txt') as f:
    lines = f.readlines()

inclination = lines[1][8:15] #Degrees
RAAN = lines[1][16:24] #Degrees
eccentricity_decimal_point = lines[1][25:32] #Decimal point assumed
str1 = "0."
ecc = str1 + eccentricity_decimal_point
eccentricity = float(ecc)
arg_of_perigee = lines[1][33:40] #Degrees
mean_anomaly = lines[1][42:49] #Degrees
mean_motion = lines[1][50:61] #Revs per day
rev_number_at_epoch = lines[1][61:66] #Revs

mean_motion_rad_s = float(mean_motion)*2*m.pi/86400
orbit_period = mean_motion_rad_s*2*m.pi
grav_parameter = 3.986004418*(10**14)
print(grav_parameter)
semi_major_axis = ((orbit_period**2)*grav_parameter/(4*(m.pi**2)))**(1/3)

def Kepler_Solver_NR(mean_anomaly, eccentricity):
    M1 = mean_anomaly * (m.pi / 180)
    tol = 1e-13
    E = M1 + ((eccentricity * m.sin(M1)) / (1 - m.sin(M1 + eccentricity) + m.sin(M1)))
    mean_anomaly = E - eccentricity * m.sin(E)
    while abs(M1 - mean_anomaly) > tol:
        E = E + (M1 - (E - eccentricity * m.sin(E))) / (1 - eccentricity * m.cos(E))
        mean_anomaly = E - eccentricity * m.sin(E)
    nu = m.acos((eccentricity - m.cos(E)) / (eccentricity * m.cos(E) - 1))
    # check half=plane
    if mean_anomaly >= 0 and mean_anomaly <= m.pi:
        nu = nu
    else:
        nu = 2 * m.pi - nu
    nu = nu * (180 / m.pi)
    #print("true anomaly, nu = " + str(nu) + " radians")
    #print("eccentric anomaly, E = " + str(E) + " radians")
    return [E, nu]

eccentric_anomaly, true_anomaly = Kepler_Solver_NR(float(mean_anomaly), float(eccentricity))
eccentric_anomaly_deg = eccentric_anomaly*180/m.pi

file = open("orbital_elements.txt", "w")
file.write("Semi-major Axis: " + str(semi_major_axis) + "\n" + "Eccentricity: " + str(eccentricity) + "\n" + "Inclination: " + inclination + "\n" + "RAAN: " + RAAN + "\n" + "Argument of Perigee: " + arg_of_perigee + "\n" + "Eccentric Anomaly: " + str(eccentric_anomaly_deg) + "\n")
file.close





