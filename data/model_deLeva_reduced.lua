return {
metadata = {
  {scaling = "deLeva",
  subject_age = 1337,
  subject_height = 1.9,
  subject_gender =  male,
  subject_weight = 86.0,
  subject_ankleHeight =  0.08698150726064047,
  subject_shoulderWidth = 0.449630251177702,
  subject_hipCenterWidth = 0.2539306288858127 },
},
gravity = { 0, 0, -9.81,},
configuration = {
  axis_front = { 1, 0, 0,},
  axis_right = { 0, -1, 0,},
  axis_up = { 0, 0, 1,},
},
animation_settings = {  force_scale = 0.002,
  torque_scale = 0.002,
  force_color = {1., 1., 0.},
  torque_color = {0., 1., 0.},
  force_transparency = 0.0,
  torque_transparency = 0.0,
},
points = {
},
frames = {
  {
  name   = "Pelvis",
  parent = "ROOT",
  visuals = {{
    src  = "meshes/pelvis.obj",
    dimensions  =    { 0.2539306288858127, 0.3047167546629752, 0.14015175687556886,},
    mesh_center =    { 0.0, 0.0, 0.02335862614592814,},
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
    mass = 5.880640175090562,
    com =    { 0.0, 0.0, 0.036299305030772326,},
    inertia = 
      {{ 0.019417325570707394, 0.0, 0.0,},
       { 0.0, 0.015586276582966052, 0.0,},
       { 0.0, 0.0, 0.017689492906532024,},},
  },
  markers = {
    LV5 =  { -0.08516625194803741, 0.001404681499481201, 0.09343450458371101,},
    L_IAS =  { 0.08607073753357057, 0.14268370474878947, 0.07617918866574454,},
    L_IPS =  { -0.0967210420277912, 0.035340500754038495, 0.062183738551812195,},
    R_IPS =  { -0.0913949669138582, -0.06728750316238402, 0.06266958091834866,},
    R_IAS =  { 0.10204527140808076, -0.11073670234044393, 0.07617918866574454,},
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
  name   = "Thigh_R",
  parent = "Pelvis",
  visuals = {{
    src  = "meshes/thighR.obj",
    dimensions  =    { 0.1970464874812943, 0.1477848656109707, 0.5911394624438828,},
    mesh_center =    { 0.0, 0.0, -0.24630810935161787,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, -0.09141502639889257, 0.0,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 13.563676675247576,
    com =    { 0.0, 0.0, -0.20172634155897504,},
    inertia = 
      {{ 0.356276056962716, 0.0, 0.0,},
       { 0.0, 0.356276056962716, 0.0,},
       { 0.0, 0.0, 0.0730747567061396,},},
  },
  markers = {
    R_FTC =  { 0.0, -0.10348185615148145, -0.0957039695780718,},
    R_FLE =  { 0.0, -0.051740928075740725, -0.48528980641076225,},
    R_FME =  { 0.0, 0.051740928075740725, -0.502901778863563,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "Thigh_L",
  parent = "Pelvis",
  visuals = {{
    src  = "meshes/thighL.obj",
    dimensions  =    { 0.1970464874812943, 0.1477848656109707, 0.5911394624438828,},
    mesh_center =    { 0.0, 0.0, -0.24630810935161787,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.09141502639889257, 0.0,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 13.563676675247576,
    com =    { 0.0, 0.0, -0.20172634155897504,},
    inertia = 
      {{ 0.356276056962716, 0.0, 0.0,},
       { 0.0, 0.356276056962716, 0.0,},
       { 0.0, 0.0, 0.0730747567061396,},},
  },
  markers = {
    L_FTC =  { 0.0, 0.09883058984289789, -0.14784207362267274,},
    L_FLE =  { 0.0, 0.04941529492144894, -0.49849603944298976,},
    L_FME =  { 0.0, -0.04941529492144894, -0.49772377564904435,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "Shank_R",
  parent = "Thigh_R",
  visuals = {{
    src  = "meshes/shankR.obj",
    dimensions  =    { 0.09620384090780759, 0.09620384090780759, 0.5772230454468454,},
    mesh_center =    { 0.0, 0.0, -0.24050960226951895,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.49261621870323574,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 3.8835180205509205,
    com =    { 0.0, 0.0, -0.21140794039490715,},
    inertia = 
      {{ 0.05661057932661182, 0.0, 0.0,},
       { 0.0, 0.054377641918846385, 0.0,},
       { 0.0, 0.0, 0.009348684422692806,},},
  },
  markers = {
    R_FAX =  { 0.0, -0.051740928075740725, -0.047799526307102866,},
    R_TTC =  { 0.044597633995881035, 0.0, -0.10467188566080729,},
    R_FAL =  { 0.0, -0.04605324082023483, -0.4766302737782796,},
    R_TAM =  { 0.0, 0.04605324082023483, -0.46825823322041826,},
  },
  joint  =
    { { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},}
  },
  {
  name   = "Shank_L",
  parent = "Thigh_L",
  visuals = {{
    src  = "meshes/shankL.obj",
    dimensions  =    { 0.09620384090780759, 0.09620384090780759, 0.5772230454468454,},
    mesh_center =    { 0.0, 0.0, -0.24050960226951895,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.49261621870323574,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 3.8835180205509205,
    com =    { 0.0, 0.0, -0.21140794039490715,},
    inertia = 
      {{ 0.05661057932661182, 0.0, 0.0,},
       { 0.0, 0.054377641918846385, 0.0,},
       { 0.0, 0.0, 0.009348684422692806,},},
  },
  markers = {
    L_FAX =  { 0.0, 0.04941529492144894, -0.039591742146375,},
    L_TTC =  { 0.0343930927913431, 0.0, -0.0887975401204427,},
    L_FAL =  { 0.0, 0.04351969573075475, -0.46157880435180665,},
    L_TAM =  { 0.0, -0.04351969573075475, -0.4578821696268718,},
  },
  joint  =
    { { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},}
  },
  {
  name   = "Foot_R",
  parent = "Shank_R",
  visuals = {{
    src  = "meshes/FullFootR.obj",
    dimensions  =    { 0.2770821772345692, 0.10519342176823013, 0.08312465317037075,},
    mesh_center =    { 0.0692705443086423, 0.0, -0.05541643544691384,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.4810192045390379,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.2074380348543827,
    com =    { 0.1223317812490623, 0.0, 0.0,},
    inertia = 
      {{ 0.006122774742027313, 0.0, 0.0,},
       { 0.0, 0.005564346983151741, 0.0,},
       { 0.0, 0.0, 0.0014253627524021854,},},
  },
  markers = {
    R_FCC =  { -0.06262835646565584, 0.0, -0.03237890154774983,},
    R_FM1 =  { 0.1495448270417365, 0.04688820512769778, -0.04032229427337646,},
    R_FM5 =  { 0.1462604673797949, -0.04688820512769778, -0.05801792774963379,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "Foot_L",
  parent = "Shank_L",
  visuals = {{
    src  = "meshes/FullFootL.obj",
    dimensions  =    { 0.2770821772345692, 0.10519342176823013, 0.08312465317037075,},
    mesh_center =    { 0.0692705443086423, 0.0, -0.05541643544691384,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.4810192045390379,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.2074380348543827,
    com =    { 0.1223317812490623, 0.0, 0.0,},
    inertia = 
      {{ 0.006122774742027313, 0.0, 0.0,},
       { 0.0, 0.005564346983151741, 0.0,},
       { 0.0, 0.0, 0.0014253627524021854,},},
  },
  markers = {
    L_FCC =  { -0.059203260264077226, 0.0, -0.025768874654134116,},
    L_FM1 =  { 0.1531218418353908, -0.04077297967916081, -0.036611440574646,},
    L_FM5 =  { 0.1384103211321455, 0.04077297967916081, -0.05168297411600749,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "MiddleTrunk",
  parent = "Pelvis",
  visuals = {{
    src  = "meshes/middleTrunk.obj",
    dimensions  =    { 0.2539306288858127, 0.3047167546629752, 0.2985319829101562,},
    mesh_center =    { 0.0, 0.0, 0.1243883262125651,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, 0.09343450458371257,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 15.476481321018086,
    com =    { 0.0, 0.0, 0.1367774035033366,},
    inertia = 
      {{ 0.222528450331019, 0.0, 0.0,},
       { 0.0, 0.14050410569121935, 0.0,},
       { 0.0, 0.0, 0.209789222401909,},},
  },
  markers = {
    SXS =  { 0.10563572660827575, 0.007578446392059326, 0.19479163354492188,},
    MAI =  { -0.16797116773987253, 0.0031296687126159666, 0.2487766524251302,},
    LV1 =  { -0.0874374027048733, 0.00824283119837443, 0.0784772451171875,},
    LV3 =  { -0.07995877624002977, 0.004831877778371175, 0.03788986368815104,},
  },
  joint  =
    {{ 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "UpperTrunk",
  parent = "MiddleTrunk",
  visuals = {{
    src  = "meshes/upperTrunk.obj",
    dimensions  =    { 0.2539306288858127, 0.449630251177702, 0.18421118782552084,},
    mesh_center =    { 0.0, 0.0, 0.09210559391276042,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, 0.2487766524251302,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 12.462001856116952,
    com =    { 0.0, 0.0, 0.11361225009138996,},
    inertia = 
      {{ 0.1685088054030286, 0.0, 0.0,},
       { 0.0, 0.06766121624652537, 0.0,},
       { 0.0, 0.0, 0.1428715476846186,},},
  },
  markers = {
    SJN =  { 0.061467258117674464, 0.002749935513178559, 0.14980222013346356,},
    CV7 =  { -0.05497700606282632, 0.0047580468514759194, 0.23026398478190102,},
    TV2 =  { -0.07911130151367436, 0.01059778213183109, 0.19361636303710938,},
    R_SAE =  { 0.0, -0.2248151255888515, 0.13926732779947917,},
    L_SAE =  { 0.0, 0.2248151255888515, 0.16984845955403646,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "UpperArm_R",
  parent = "UpperTrunk",
  visuals = {{
    src  = "meshes/upperArm.obj",
    dimensions  =    { 0.1484417778641116, 0.1187534222912893, 0.32657191130104557,},
    mesh_center =    { 0.0, 0.0, -0.1484417778641116,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, -0.224815125588851, 0.07812075097654564,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 2.3447270018339035,
    com =    { 0.0, 0.0, -0.17136118836633046,},
    inertia = 
      {{ 0.016786273333036263, 0.0, 0.0,},
       { 0.0, 0.01495440473563358, 0.0,},
       { 0.0, 0.0, 0.005159157001981131,},},
  },
  markers = {
    R_HUM =  { 0.0, -0.050817433333184135, -0.19854767739966966,},
    R_HLE =  { 0.0, -0.03811307499988639, -0.2934923850277574,},
    R_HME =  { 0.0, 0.03811307499988639, -0.3073287429169682,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "UpperArm_L",
  parent = "UpperTrunk",
  visuals = {{
    src  = "meshes/upperArm.obj",
    dimensions  =    { 0.1484417778641116, 0.1187534222912893, 0.32657191130104557,},
    mesh_center =    { 0.0, 0.0, -0.1484417778641116,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.224815125588851, 0.07812075097654564,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 2.3447270018339035,
    com =    { 0.0, 0.0, -0.17136118836633046,},
    inertia = 
      {{ 0.016786273333036263, 0.0, 0.0,},
       { 0.0, 0.01495440473563358, 0.0,},
       { 0.0, 0.0, 0.005159157001981131,},},
  },
  markers = {
    L_HUM =  { 0.0, 0.04861366212452536, -0.19307372531756503,},
    L_HLE =  { 0.0, 0.03646024659339361, -0.3002747264286892,},
    L_HME =  { 0.0, -0.03646024659339361, -0.3212578670964923,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "LowerArm_R",
  parent = "UpperArm_R",
  visuals = {{
    src  = "meshes/lowerArm.obj",
    dimensions  =    { 0.11420750708630552, 0.08565563031472913, 0.3140706444873402,},
    mesh_center =    { 0.0, 0.0, -0.1427593838578819,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.2968835557282232,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.4121556596315403,
    com =    { 0.0, 0.0, -0.13059628435319035,},
    inertia = 
      {{ 0.008769403556068289, 0.0, 0.0,},
       { 0.0, 0.008084322683324086, 0.0,},
       { 0.0, 0.0, 0.0016854762322043133,},},
  },
  markers = {
    R_RSP =  { 0.03811307499988639, 0.0, -0.28698527909663635,},
    R_USP =  { -0.03811307499988639, 0.0, -0.28827083940835496,},
  },
  joint  =
    {{ 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "LowerArm_L",
  parent = "UpperArm_L",
  visuals = {{
    src  = "meshes/lowerArm.obj",
    dimensions  =    { 0.11420750708630552, 0.08565563031472913, 0.3140706444873402,},
    mesh_center =    { 0.0, 0.0, -0.1427593838578819,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.2968835557282232,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 1.4121556596315403,
    com =    { 0.0, 0.0, -0.13059628435319035,},
    inertia = 
      {{ 0.008769403556068289, 0.0, 0.0,},
       { 0.0, 0.008084322683324086, 0.0,},
       { 0.0, 0.0, 0.0016854762322043133,},},
  },
  markers = {
    L_RSP =  { 0.03646024659339361, 0.0, -0.28444248461014715,},
    L_USP =  { -0.03646024659339361, 0.0, -0.2827666960231725,},
  },
  joint  =
    {{ 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
  {
  name   = "Hand_R",
  parent = "LowerArm_R",
  visuals = {{
    src  = "meshes/handR.obj",
    dimensions  =    { 0.10739049164772821, 0.04602449642045495, 0.15341498806818316,},
    mesh_center =    { 0.0, 0.0, -0.07670749403409158,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.2855187677157638,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.40887875314401423,
    com =    { 0.0, 0.0, -0.05559759167590957,},
    inertia = 
      {{ 0.0007982062065274877, 0.0, 0.0,},
       { 0.0, 0.0005314542071214375, 0.0,},
       { 0.0, 0.0, 0.000325811021028581,},},
  },
  markers = {
    R_HM2 =  { 0.03811307499988639, -0.025, -0.08060912791277001,},
  },
  joint  =
    {}
  },
  {
  name   = "Hand_L",
  parent = "LowerArm_L",
  visuals = {{
    src  = "meshes/handL.obj",
    dimensions  =    { 0.10739049164772821, 0.04602449642045495, 0.15341498806818316,},
    mesh_center =    { 0.0, 0.0, -0.07670749403409158,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, -0.2855187677157638,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 0.40887875314401423,
    com =    { 0.0, 0.0, -0.05559759167590957,},
    inertia = 
      {{ 0.0007982062065274877, 0.0, 0.0,},
       { 0.0, 0.0005314542071214375, 0.0,},
       { 0.0, 0.0, 0.000325811021028581,},},
  },
  markers = {
    L_HM2 =  { 0.03646024659339361, 0.025, -0.07280586015541311,},
  },
  joint  =
    {}
  },
  {
  name   = "Head",
  parent = "UpperTrunk",
  visuals = {{
    src  = "meshes/head.obj",
    dimensions  =    { 0.19517581522623695, 0.19517581522623695, 0.22305807454427085,},
    mesh_center =    { 0.0, 0.0, 0.11152903727213542,},
    color       =    { 0.2, 0.7, 0.3,},
    },},
  joint_frame = {
    r =    { 0.0, 0.0, 0.23026398478190105,},
    E = 
      {{ 1.0, 0.0, 0.0,},
       { 0.0, 1.0, 0.0,},
       { 0.0, 0.0, 1.0,},},
  },
  body = {
    mass = 6.540088357249719,
    com =    { 0.0, 0.0, 0.1393555320715332,},
    inertia = 
      {{ 0.04667934965807549, 0.0, 0.0,},
       { 0.0, 0.05044993921971202, 0.0,},
       { 0.0, 0.0, 0.03463542766022678,},},
  },
  markers = {
    L_HEAD =  { 0.030250180216472078, 0.08540846827380116, 0.16082055997721356,},
    R_HEAD =  { 0.02356554455566475, -0.0925900482718122, 0.15790633715820312,},
    SGL =  { 0.15164229086303269, 0.00011461255582174076, 0.1889350534667969,},
  },
  joint  =
    {{ 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,},
     { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,},},
  },
},
}