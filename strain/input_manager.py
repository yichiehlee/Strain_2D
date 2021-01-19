# The input manager for GPS Strain analysis. 

from Strain_2D.strain import velocity_io

# ----------------- INPUTS -------------------------
def inputs(MyParams):
    print("------------------------------");
    # Purpose: generate input velocity field.
    myVelfield = velocity_io.read_stationvels(MyParams.input_file);
    myVelfield = clean_velfield(myVelfield, coord_box=MyParams.range_data);
    if len(myVelfield) == 0:
        raise Exception("Error! Velocity field has no velocities.");
    for item in myVelfield:
        if item.se == 0 or item.sn == 0 or item.su == 0:
            raise Exception("Error! Velocity uncertainty cannot be zero.");
    return myVelfield;


def clean_velfield(myVelfield, coord_box=(-180, 180, -90, 90)):
    print("%d stations before applying cleaning." % (len(myVelfield)));
    select_velfield = [];
    for station_vel in myVelfield:
        if coord_box[0] < station_vel.elon < coord_box[1] and coord_box[2] < station_vel.nlat < coord_box[3]:
            # The station is within the box of interest.
            select_velfield.append(station_vel);
    print("%d stations after selection criteria.\n" % (len(select_velfield)));
    return select_velfield;
