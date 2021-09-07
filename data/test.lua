return {
metadata = {
  {scaling = "deLeva",
  subject_age = None,
  subject_height = 160,
  subject_sex = female,
  subject_mass = 60,
  subject_shoulderWidth = 354.38 mm,
  subject_AsisDist = 259.22 mm },
},
gravity = { 0, 0, -9.81,},
configuration = {
  axis_right = { 0, 1, 0,},
  axis_up = { 0, 0, 1,},
  axis_front = { 1, 0, 0,},
frames = {
  {
  name   = "Pelvis",
  parent = "ROOT",
  visuals = {{
    src  = "meshes/Pelvis.obj",
    dimensions  =    { 0.25922, 0.311064, 0.0,},
    mesh_center =    { 0.0, 0.0, 0.0,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, 0.0,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 7.2604999999999995,
    com =    { 0.0, 0.0, 0.0,},
    inertia = 
      {{ 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},},
  },
  markers = {
    R_IPS =  { 0.00, -86.46, -7.71,},
    R_IAS =  { 174.08, -128.09, 1.12,},
    L_IPS =  { 0.00, 86.46, 7.71,},
    L_IAS =  { 171.63, 130.44, 20.05,},
  },
  joint  =
    {{ 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,},
     { 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,},
     { 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,},
     { 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "MiddleTrunk",
  parent = "Pelvis",
  visuals = {{
    src  = "meshes/MiddleTrunk.obj",
    dimensions  =    { 0.25922, 0.311064, 0.0,},
    mesh_center =    { 0.0, 0.0, 0.0,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, 0.0,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 10.6145,
    com =    { 0.0, 0.0, 0.0,},
    inertia = 
      {{ 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},},
  },
  markers = {
    LV5 =  { -10.69, 3.98, 8.51,},
    LV3 =  { 0.00, 0.00, 70.79,},
    LV1 =  { -3.03, -4.96, 113.38,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "UpperTrunk",
  parent = "MiddleTrunk",
  visuals = {{
    src  = "meshes/UpperTrunk.obj",
    dimensions  =    { 0.25922, 0.35438, 90.82310507794809,},
    mesh_center =    { 0.0, 0.0, 45.41155253897404,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { -3.03, -4.96, 113.38,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 10.373999999999999,
    com =    { 0.0, 0.0, 56.015150056824474,},
    inertia = 
      {{ 34099.005821122504, 0.0, 0.0,},
       { 0.0, 13691.748636733437, 0.0,},
       { 0.0, 0.0, 28911.116689235227,},},
  },
  markers = {
    MAI =  { 0.00, 0.00, 86.32,},
    SXS =  { 199.25, -2.17, -24.41,},
    SJN =  { 231.53, -11.08, 224.52,},
    TV2 =  { 125.51, -12.50, 316.35,},
    CV7 =  { 148.88, -15.25, 331.38,},
    R_SAE =  { 178.38, -189.10, 242.74,},
    L_SAE =  { 194.30, 164.44, 261.17,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "Head",
  parent = "UpperTrunk",
  visuals = {{
    src  = "meshes/Head.obj",
    dimensions  =    { 186.13489940900388, 186.13489940900388, 212.7255993245759,},
    mesh_center =    { 0.0, 0.0, 106.36279966228796,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 148.88, -15.25, 331.38,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 4.511,
    com =    { 0.0, 0.0, 132.90031817802878,},
    inertia = 
      {{ 29283.138522536352, 0.0, 0.0,},
       { 0.0, 31648.5248711855, 0.0,},
       { 0.0, 0.0, 21727.68115646286,},},
  },
  markers = {
    R_HEAD =  { -72.26, -81.70, 131.51,},
    SGL =  { 0.00, 0.00, 250.95,},
    L_HEAD =  { -42.72, 101.13, 149.78,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "R_UpperArm",
  parent = "UpperTrunk",
  visuals = {{
    src  = "meshes/R_UpperArm.obj",
    dimensions  =    { 127.66809595588086, 102.13447676470469, 280.8698111029379,},
    mesh_center =    { 0.0, 0.0, -127.66809595588086,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 156.43, -190.43, 186.66,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.7614999999999998,
    com =    { 0.0, 0.0, -147.38004997146888,},
    inertia = 
      {{ 9328.184376787425, 0.0, 0.0,},
       { 0.0, 8310.209291335366, 0.0,},
       { 0.0, 0.0, 2866.9596156616976,},},
  },
  markers = {
    R_HUM =  { 30.91, -39.88, -112.77,},
    R_HME =  { 8.74, 17.98, -257.60,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "R_Forearm",
  parent = "R_UpperArm",
  visuals = {{
    src  = "meshes/R_Forearm.obj",
    dimensions  =    { 197.2628012778892, 147.94710095841688, 542.4727035141952,},
    mesh_center =    { 0.0, 0.0, -246.57850159736148,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 8.74, -12.64, -248.98,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.053,
    com =    { 0.0, 0.0, -225.57001326126627,},
    inertia = 
      {{ 19508.188570603575, 0.0, 0.0,},
       { 0.0, 17984.175361933365, 0.0,},
       { 0.0, 0.0, 3749.466877523195,},},
  },
  markers = {
    R_HLE =  { 0.00, -31.80, -0.98,},
    R_RSP =  { 29.92, -8.67, -240.23,},
    R_USP =  { -29.92, 8.67, -230.05,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "R_Hand",
  parent = "R_Forearm",
  visuals = {{
    src  = "meshes/R_Hand.obj",
    dimensions  =    { 14.476683736270543, 6.204293029830233, 20.680976766100777,},
    mesh_center =    { 0.0, 0.0, -10.340488383050388,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -235.14,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.3965,
    com =    { 0.0, 0.0, -7.494785980034922,},
    inertia = 
      {{ 14.065988583628801, 0.0, 0.0,},
       { 0.0, 9.365285247045005, 0.0,},
       { 0.0, 0.0, 5.741441327731202,},},
  },
  markers = {
    R_HM2 =  { 0.00, 0.00, -97.72,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "L_UpperArm",
  parent = "UpperTrunk",
  visuals = {{
    src  = "meshes/L_UpperArm.obj",
    dimensions  =    { 129.82333515204422, 103.85866812163539, 285.6113373344973,},
    mesh_center =    { 0.0, 0.0, -129.82333515204422,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 172.35, 163.11, 205.09,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.7614999999999998,
    com =    { 0.0, 0.0, -149.86805809951986,},
    inertia = 
      {{ 9645.79177972127, 0.0, 0.0,},
       { 0.0, 8593.156527822852, 0.0,},
       { 0.0, 0.0, 2964.5742811814325,},},
  },
  markers = {
    L_HUM =  { 13.19, 53.46, -142.45,},
    L_HME =  { 1.15, -8.87, -266.66,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "L_Forearm",
  parent = "L_UpperArm",
  visuals = {{
    src  = "meshes/L_Forearm.obj",
    dimensions  =    { 205.09682895647117, 153.82262171735337, 564.0162796302957,},
    mesh_center =    { 0.0, 0.0, -256.37103619558894,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 1.15, 22.53, -257.33,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.053,
    com =    { 0.0, 0.0, -234.52822391172475,},
    inertia = 
      {{ 21088.439500840348, 0.0, 0.0,},
       { 0.0, 19440.974374429137, 0.0,},
       { 0.0, 0.0, 4053.1905420579124,},},
  },
  markers = {
    L_HLE =  { 0.00, 32.75, -0.73,},
    L_USP =  { 27.75, 10.49, -237.51,},
    L_RSP =  { -27.75, -10.49, -234.27,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "L_Hand",
  parent = "L_Forearm",
  visuals = {{
    src  = "meshes/L_Hand.obj",
    dimensions  =    { 21.785603732740572, 9.336687314031673, 31.122291046772247,},
    mesh_center =    { 0.0, 0.0, -15.561145523386124,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -235.89,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.3965,
    com =    { 0.0, 0.0, -11.278718275350263,},
    inertia = 
      {{ 31.854536243711998, 0.0, 0.0,},
       { 0.0, 21.2090900373625, 0.0,},
       { 0.0, 0.0, 13.002353142687998,},},
  },
  markers = {
    L_HM2 =  { 0.00, 0.00, -98.31,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "R_Thigh",
  parent = "Pelvis",
  visuals = {{
    src  = "meshes/R_Thigh.obj",
    dimensions  =    { 70.52448959049615, 52.89336719287211, 211.57346877148845,},
    mesh_center =    { 0.0, 0.0, -88.15561198812019,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 139.65, -63.14, -87.16,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 9.204,
    com =    { 0.0, 0.0, -72.19944621827042,},
    inertia = 
      {{ 30969.081619171226, 0.0, 0.0,},
       { 0.0, 30969.081619171226, 0.0,},
       { 0.0, 0.0, 6351.979204065191,},},
  },
  markers = {
    R_FME =  { -44.60, 18.81, -417.42,},
    R_FLE =  { -36.27, -92.22, -404.68,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "R_Shank",
  parent = "R_Thigh",
  visuals = {{
    src  = "meshes/R_Shank.obj",
    dimensions  =    { 74.30548084764676, 74.30548084764676, 445.8328850858806,},
    mesh_center =    { 0.0, 0.0, -185.7637021191169,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { -40.43, -36.7, -411.05,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 2.8145,
    com =    { 0.0, 0.0, -163.28629416270377,},
    inertia = 
      {{ 24475.434058380106, 0.0, 0.0,},
       { 0.0, 23510.029483292816, 0.0,},
       { 0.0, 0.0, 4041.8789534037005,},},
  },
  markers = {
    R_FAX =  { -29.64, -65.32, -41.71,},
    R_TTC =  { 18.93, -18.64, -55.89,},
    R_TAM =  { 16.06, 38.04, -366.05,},
    R_FAL =  { -16.06, -38.04, -377.56,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "R_Foot",
  parent = "R_Shank",
  visuals = {{
    src  = "meshes/R_Foot.obj",
    dimensions  =    { 67.24609579745132, 0.09334800000000001, 20.173828739235393,},
    mesh_center =    { 16.81152394936283, 0.0, -13.449219159490264,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -371.8,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.8905000000000001,
    com =    { 29.689151294574756, 0.0, 0.0,},
    inertia = 
      {{ 265.9710209511303, 0.0, 0.0,},
       { 0.0, 241.71313013961748, 0.0,},
       { 0.0, 0.0, 61.91721930906721,},},
  },
  markers = {
    R_FM5 =  { 123.45, -46.99, -5.04,},
    R_FM1 =  { 124.57, 46.99, 5.04,},
    R_FCC =  { -48.92, -10.10, -41.11,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "L_Thigh",
  parent = "Pelvis",
  visuals = {{
    src  = "meshes/L_Thigh.obj",
    dimensions  =    { 69.86522682994739, 52.39892012246053, 209.59568048984212,},
    mesh_center =    { 0.0, 0.0, -87.33153353743423,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 136.73, 77.79, -75.9,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 9.204,
    com =    { 0.0, 0.0, -71.52452596715862,},
    inertia = 
      {{ 30392.790051928667, 0.0, 0.0,},
       { 0.0, 30392.790051928667, 0.0,},
       { 0.0, 0.0, 6233.777699234747,},},
  },
  markers = {
    L_FLE =  { -28.48, 86.87, -398.82,},
    L_FME =  { -49.42, -18.32, -417.67,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "L_Shank",
  parent = "L_Thigh",
  visuals = {{
    src  = "meshes/L_Shank.obj",
    dimensions  =    { 75.68548827879755, 75.68548827879755, 454.1129296727853,},
    mesh_center =    { 0.0, 0.0, -189.21372069699387,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { -38.95, 34.27, -408.24,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 2.8145,
    com =    { 0.0, 0.0, -166.31886049265762,},
    inertia = 
      {{ 25392.995681279182, 0.0, 0.0,},
       { 0.0, 24391.398972211413, 0.0,},
       { 0.0, 0.0, 4193.4052962338465,},},
  },
  markers = {
    L_FAX =  { -35.57, 64.57, -42.81,},
    L_TTC =  { 14.00, 23.36, -71.79,},
    L_FAL =  { -19.92, 33.19, -384.20,},
    L_TAM =  { 19.92, -33.19, -376.65,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "L_Foot",
  parent = "L_Shank",
  visuals = {{
    src  = "meshes/L_Foot.obj",
    dimensions  =    { 58.868393896895135, 0.09334800000000001, 17.66051816906854,},
    mesh_center =    { 14.717098474223784, 0.0, -11.773678779379027,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -380.42,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.8905000000000001,
    com =    { 25.990395905479204, 0.0, 0.0,},
    inertia = 
      {{ 203.82832929680916, 0.0, 0.0,},
       { 0.0, 185.23816357614754, 0.0,},
       { 0.0, 0.0, 47.45059563759841,},},
  },
  markers = {
    L_FCC =  { -42.89, 4.92, -40.91,},
    L_FM1 =  { 143.42, -47.75, 8.49,},
    L_FM5 =  { 139.75, 47.75, -8.49,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
},
}