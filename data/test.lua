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
    mass = 0.12087237479806139,
    com =    { 0.0, 0.0, 0.0,},
    inertia = 
      {{ 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},},
  },
  markers = {
    R_IPS =  { 0.0, -0.08646, -0.00771,},
    R_IAS =  { 0.17408, -0.12809, 0.0011200000000000001,},
    L_IPS =  { 0.0, 0.08646, 0.00771,},
    L_IAS =  { 0.17163, 0.13044, 0.020050000000000002,},
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
    mass = 0.1420032310177706,
    com =    { 0.0, 0.0, 0.0,},
    inertia = 
      {{ 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},
       { 0.0, 0.0, 0.0,},},
  },
  markers = {
    LV5 =  { -0.01069, 0.00398, 0.00851,},
    LV3 =  { 0.0, 0.0, 0.07079,},
    LV1 =  { -0.0030299999999999997, -0.00496, 0.11338,},
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
    dimensions  =    { 0.25922, 0.35438, 0.0908231050779481,},
    mesh_center =    { 0.0, 0.0, 0.04541155253897405,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { -0.0030299999999999997, -0.00496, 0.11338,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.14975767366720516,
    com =    { 0.0, 0.0, 0.056196796266980376,},
    inertia = 
      {{ 0.000419154019925771, 0.0, 0.0,},
       { 0.0, 0.0001903097761452657, 0.0,},
       { 0.0, 0.0, 0.0003891297941160058,},},
  },
  markers = {
    MAI =  { 0.0, 0.0, 0.08632,},
    SXS =  { 0.19925, -0.00217, -0.02441,},
    SJN =  { 0.23153, -0.01108, 0.22452,},
    TV2 =  { 0.12551, -0.0125, 0.31635,},
    CV7 =  { 0.14887999999999998, -0.01525, 0.33138,},
    R_SAE =  { 0.17837999999999998, -0.1891, 0.24274,},
    L_SAE =  { 0.1943, 0.16444, 0.26117,},
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
    dimensions  =    { 79.24094707987427, 79.24094707987427, 90.5610823769992,},
    mesh_center =    { 0.0, 0.0, 45.2805411884996,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.14887999999999998, -0.01525, 0.33138,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.06484652665589662,
    com =    { 0.0, 0.0, 58.40057799786735,},
    inertia = 
      {{ 61.02791545850441, 0.0, 0.0,},
       { 0.0, 72.31593173808018, 0.0,},
       { 0.0, 0.0, 56.607108140531565,},},
  },
  markers = {
    R_HEAD =  { -0.07226, -0.08170000000000001, 0.13151,},
    SGL =  { 0.0, 0.0, 0.25095,},
    L_HEAD =  { -0.04272, 0.10113, 0.14978,},
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
    dimensions  =    { 56.669291407439964, 45.33543312595197, 124.67244109636793,},
    mesh_center =    { 0.0, 0.0, -56.669291407439964,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.15643, -0.19043000000000002, 0.18666,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.024717285945072696,
    com =    { 0.0, 0.0, -65.21502055168192,},
    inertia = 
      {{ 24.538382364162125, 0.0, 0.0,},
       { 0.0, 21.463623102030944, 0.0,},
       { 0.0, 0.0, 6.9547218998060005,},},
  },
  markers = {
    R_HUM =  { 0.03091, -0.039880000000000006, -0.11277,},
    R_HME =  { 0.00874, 0.01798, -0.2576,},
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
    dimensions  =    { 123.716675269907, 92.78750645243025, 340.22085699224425,},
    mesh_center =    { 0.0, 0.0, -154.64584408738375,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.00874, -0.01264, -0.24897999999999998,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.013376413570274637,
    com =    { 0.0, 0.0, -141.0060806388765,},
    inertia = 
      {{ 87.1680238775518, 0.0, 0.0,},
       { 0.0, 84.51668074585542, 0.0,},
       { 0.0, 0.0, 11.306596482465723,},},
  },
  markers = {
    R_HLE =  { 0.0, -0.0318, -0.00098,},
    R_RSP =  { 0.029920000000000002, -0.00867, -0.24023,},
    R_USP =  { -0.029920000000000002, 0.00867, -0.23005,},
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
    dimensions  =    { 174.45337389241172, 74.76573166817646, 249.2191055605882,},
    mesh_center =    { 0.0, 0.0, -124.6095527802941,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.23514,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.0054281098546042,
    com =    { 0.0, 0.0, -85.40738747561358,},
    inertia = 
      {{ 20.07201380863175, 0.0, 0.0,},
       { 0.0, 14.586058946127448, 0.0,},
       { 0.0, 0.0, 7.9956308701543675,},},
  },
  markers = {
    R_HM2 =  { 0.0, 0.0, -0.09772,},
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
    dimensions  =    { 56.66802792382734, 45.334422339061874, 124.66966143242016,},
    mesh_center =    { 0.0, 0.0, -56.66802792382734,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.17235, 0.16311, 0.20509,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.024717285945072696,
    com =    { 0.0, 0.0, -65.21356653474051,},
    inertia = 
      {{ 24.53728817372492, 0.0, 0.0,},
       { 0.0, 21.46266601811247, 0.0,},
       { 0.0, 0.0, 6.954411781963544,},},
  },
  markers = {
    L_HUM =  { 0.01319, 0.05346, -0.14245,},
    L_HME =  { 0.00115, -0.00887, -0.26666,},
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
    dimensions  =    { 125.51919369113382, 94.13939526835036, 345.17778265061804,},
    mesh_center =    { 0.0, 0.0, -156.89899211391727,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.00115, 0.02253, -0.25733,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.013376413570274637,
    com =    { 0.0, 0.0, -143.0605010094698,},
    inertia = 
      {{ 89.7265566005172, 0.0, 0.0,},
       { 0.0, 86.99739194826205, 0.0,},
       { 0.0, 0.0, 11.638464704308069,},},
  },
  markers = {
    L_HLE =  { 0.0, 0.03275, -0.00073,},
    L_USP =  { 0.02775, 0.010490000000000001, -0.23751,},
    L_RSP =  { -0.02775, -0.010490000000000001, -0.23427,},
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
    dimensions  =    { 180.6573811123673, 77.42459190530026, 258.08197301766756,},
    mesh_center =    { 0.0, 0.0, -129.04098650883378,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.23589,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.0054281098546042,
    com =    { 0.0, 0.0, -88.44469215315468,},
    inertia = 
      {{ 21.525022865238917, 0.0, 0.0,},
       { 0.0, 15.641940829778562, 0.0,},
       { 0.0, 0.0, 8.574432986294111,},},
  },
  markers = {
    L_HM2 =  { 0.0, 0.0, -0.09831000000000001,},
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
    dimensions  =    { 0.07052448959049616, 0.05289336719287211, 0.21157346877148844,},
    mesh_center =    { 0.0, 0.0, -0.08815561198812019,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.13965, -0.06314, -0.08716,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.1432633279483037,
    com =    { 0.0, 0.0, -0.06368361410021803,},
    inertia = 
      {{ 0.0006063839371344424, 0.0, 0.0,},
       { 0.0, 0.0005900621039399319, 0.0,},
       { 0.0, 0.0, 0.00011687590459938091,},},
  },
  markers = {
    R_FME =  { -0.0446, 0.01881, -0.41742,},
    R_FLE =  { -0.036270000000000004, -0.09222, -0.40468,},
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
    dimensions  =    { 35.225458424598195, 35.225458424598195, 211.35275054758918,},
    mesh_center =    { 0.0, 0.0, -88.06364606149549,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { -0.04043, -0.0367, -0.41105,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.04662358642972536,
    com =    { 0.0, 0.0, -76.65059753192567,},
    inertia = 
      {{ 103.10542496664684, 0.0, 0.0,},
       { 0.0, 100.03926467642967, 0.0,},
       { 0.0, 0.0, 12.24150032848965,},},
  },
  markers = {
    R_FAX =  { -0.02964, -0.06531999999999999, -0.041710000000000004,},
    R_TTC =  { 0.01893, -0.01864, -0.05589,},
    R_TAM =  { 0.016059999999999998, 0.03804, -0.36605,},
    R_FAL =  { -0.016059999999999998, -0.03804, -0.37756,},
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
    dimensions  =    { 414.2922384684994, 0.09334800000000001, 124.28767154054982,},
    mesh_center =    { 103.57305961712485, 0.0, -82.85844769369989,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.3718,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.012504038772213247,
    com =    { 166.29690452125567, 0.0, 0.0,},
    inertia = 
      {{ 191.86964964751527, 0.0, 0.0,},
       { 0.0, 167.05993666974913, 0.0,},
       { 0.0, 0.0, 41.46613014216446,},},
  },
  markers = {
    R_FM5 =  { 0.12345, -0.046990000000000004, -0.00504,},
    R_FM1 =  { 0.12456999999999999, 0.046990000000000004, 0.00504,},
    R_FCC =  { -0.048920000000000005, -0.0101, -0.04111,},
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
    dimensions  =    { 0.06986522682994739, 0.05239892012246054, 0.20959568048984217,},
    mesh_center =    { 0.0, 0.0, -0.08733153353743424,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.13673, 0.07779000000000001, -0.07590000000000001,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.1432633279483037,
    com =    { 0.0, 0.0, -0.0630882998274425,},
    inertia = 
      {{ 0.0005950999748336168, 0.0, 0.0,},
       { 0.0, 0.0005790818682703189, 0.0,},
       { 0.0, 0.0, 0.00011470100645216648,},},
  },
  markers = {
    L_FLE =  { -0.028480000000000002, 0.08687, -0.39882,},
    L_FME =  { -0.04942, -0.01832, -0.41767000000000004,},
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
    dimensions  =    { 34.90026077829963, 34.90026077829963, 209.4015646697978,},
    mesh_center =    { 0.0, 0.0, -87.25065194574908,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { -0.038950000000000005, 0.03427, -0.40824,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.04662358642972536,
    com =    { 0.0, 0.0, -75.94296745358,},
    inertia = 
      {{ 101.21049601531685, 0.0, 0.0,},
       { 0.0, 98.20068732740609, 0.0,},
       { 0.0, 0.0, 12.016519214375878,},},
  },
  markers = {
    L_FAX =  { -0.03557, 0.06456999999999999, -0.04281,},
    L_TTC =  { 0.014, 0.02336, -0.07179,},
    L_FAL =  { -0.01992, 0.03319, -0.3842,},
    L_TAM =  { 0.01992, -0.03319, -0.37665,},
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
    dimensions  =    { 411.145925916549, 0.09334800000000001, 123.34377777496469,},
    mesh_center =    { 102.78648147913725, 0.0, -82.22918518330981,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.38042000000000004,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.012504038772213247,
    com =    { 165.03397466290275, 0.0, 0.0,},
    inertia = 
      {{ 188.96643533699856, 0.0, 0.0,},
       { 0.0, 164.53212260564544, 0.0,},
       { 0.0, 0.0, 40.83869864035246,},},
  },
  markers = {
    L_FCC =  { -0.04289, 0.00492, -0.040909999999999995,},
    L_FM1 =  { 0.14342, -0.04775, 0.008490000000000001,},
    L_FM5 =  { 0.13975, 0.04775, -0.008490000000000001,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
},
}