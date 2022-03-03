-- ---------------------------
-- Table structure for raidboss_spawnlist
-- ---------------------------
DROP TABLE IF EXISTS raidboss_spawnlist;

CREATE TABLE raidboss_spawnlist (
  boss_id INT NOT NULL default 0,
  amount INT NOT NULL default 0,
  loc_x INT NOT NULL default 0,
  loc_y INT NOT NULL default 0,
  loc_z INT NOT NULL default 0,
  heading INT NOT NULL default 0,
  respawn_min_delay INT(11) NOT NULL default '43200',
  respawn_max_delay INT(11) NOT NULL default '129600',
  respawn_time BIGINT NOT NULL default 0,
  currentHp decimal(8,0) default NULL,
  currentMp decimal(8,0) default NULL,
  PRIMARY KEY  (boss_id,loc_x,loc_y,loc_z)
);

INSERT INTO `raidboss_spawnlist` VALUES 
(25001,1,-54390,145764,-3000,0,43200,129600,0,23712,545),
(25004,1,-94222,99620,-3612,0,43200,129600,0,66433,763),
(25007,1,123666,74788,-2912,0,43200,129600,0,100965,1062),
(25010,1,113738,52174,-3904,0,43200,129600,0,153521,2039),
(25013,1,169274,11652,-2780,0,43200,129600,0,132487,1722),
(25016,1,76787,245775,-10376,0,43200,129600,0,188376,2368),
(25019,1,6780,168876,-3772,0,43200,129600,0,52415,606),
(25020,1,89924,125024,-2232,0,43200,129600,0,39603,893),
(25023,1,25910,100388,-3792,0,43200,129600,0,73549,1415),
(25026,1,92712,7400,-4048,0,43200,129600,0,69124,1660),
(25029,1,55470,205540,-3800,0,43200,129600,0,156190,1911),
(25032,1,88532,245798,-10376,0,43200,129600,0,229722,2707),
(25035,1,180968,12035,-2720,0,43200,129600,0,241630,3058),
(25038,1,-57466,186017,-5004,0,43200,129600,0,30283,699),
(25041,1,9730,126132,-3732,0,43200,129600,0,41308,927),
(25044,1,107288,27048,-3572,0,43200,129600,0,64765,1296),
(25047,1,115898,26964,-3376,0,43200,129600,0,69124,1660),
(25050,1,125066,26388,-3740,0,43200,129600,0,126124,2039),
(25051,1,117232,-9476,-3320,0,43200,129600,0,186648,2707),
(25054,1,113090,16100,3924,0,43200,129600,0,250509,3420),
(25057,1,106638,167576,-3508,0,43200,129600,0,60514,2235),
(25060,1,-60642,188044,-4552,0,43200,129600,0,21374,575),
(25063,1,-91262,116164,-3508,0,43200,129600,0,82617,927),
(25064,1,91884,84420,-3876,0,43200,129600,0,50445,1120),
(25067,1,94308,-24156,-2352,0,43200,129600,0,140823,1598),
(25070,1,111788,42392,-4188,0,43200,129600,0,82665,2039),
(25073,1,143955,110360,-3955,32768,43200,129600,0,239476,2987),
(25076,1,-61518,126320,-3112,0,43200,129600,0,26207,606),
(25079,1,53775,102087,-1129,0,43200,129600,0,61688,763),
(25082,1,88416,139892,-3560,0,43200,129600,0,48537,1062),
(25085,1,66700,66688,-3808,0,43200,129600,0,108514,1355),
(25088,1,90398,15708,-5400,0,43200,129600,0,225544,2039),
(25089,1,165400,93248,-3260,0,43200,129600,0,91885,2301),
(25092,1,115484,15564,1904,0,43200,129600,0,196324,3058),
(25095,1,-37996,197708,-2800,0,43200,129600,0,31723,731),
(25098,1,123484,132856,-3756,0,43200,129600,0,82617,927),
(25098,1,-5937,175004,-2940,59144,43200,129600,0,82617,927),
(25099,1,64204,15618,-3660,0,43200,129600,0,58430,1355),
(25102,1,113938,84010,-2832,0,43200,129600,0,121028,1722),
(25103,1,135668,93892,-3844,0,43200,129600,0,82665,2039),
(25106,1,127916,-13600,-3836,0,43200,129600,0,98098,2570),
(25109,1,152260,110394,-5552,0,43200,129600,0,248996,3347),
(25112,1,116196,138980,-3724,0,43200,129600,0,33216,763),
(25115,1,93838,197378,-3772,0,43200,129600,0,93684,1120),
(25118,1,50755,145946,-3677,0,43200,129600,0,82617,1415),
(25119,1,121770,63216,-3792,0,43200,129600,0,163059,1722),
(25122,1,89442,-6520,-3220,0,43200,129600,0,84968,2235),
(25125,1,170542,84914,-2052,0,43200,129600,0,459444,2707),
(25126,1,116464,15154,6956,0,43200,129600,0,510317,3718),
(25127,1,-47740,218612,-2536,0,43200,129600,0,49872,763),
(25128,1,17642,178620,-3616,0,43200,129600,0,37942,860),
(25131,1,75214,-10092,-2904,0,43200,129600,0,71339,1415),
(25134,1,87536,75560,-3688,0,43200,129600,0,50445,1722),
(25137,1,125000,101612,-3480,0,43200,129600,0,82665,2039),
(25140,1,191979,54902,-7658,0,43200,129600,0,186648,2707),
(25143,1,112624,15794,6964,0,43200,129600,0,255158,3718),
(25146,1,-13714,213368,-3800,0,43200,129600,0,18330,485),
(25149,1,-12696,137645,-3720,0,43200,129600,0,26207,606),
(25152,1,42962,123164,-3312,0,43200,129600,0,41308,927),
(25155,1,73206,66332,-3836,0,43200,129600,0,100890,1120),
(25158,1,76718,4960,-3192,0,43200,129600,0,248599,1722),
(25159,1,125052,42796,-3880,0,43200,129600,0,80375,1975),
(25162,1,193302,53598,-4384,0,43200,129600,0,349842,2368),
(25163,1,130196,58772,3496,0,43200,129600,0,241630,3058),
(25166,1,-21926,151796,-3136,0,43200,129600,0,48671,606),
(25169,1,-54484,169744,-3300,0,43200,129600,0,123377,763),
(25170,1,25550,121216,-3788,0,43200,129600,0,46672,1028),
(25173,1,75694,109632,-2672,0,43200,129600,0,60514,1415),
(25176,1,92570,114556,-3348,0,43200,129600,0,82665,2039),
(25179,1,182438,50775,-4384,0,43200,129600,0,94188,2368),
(25182,1,41520,215512,-3816,0,43200,129600,0,512194,2707),
(25185,1,88092,165878,-3788,0,43200,129600,0,41308,927),
(25188,1,87836,175804,-3612,0,43200,129600,0,66433,763),
(25189,1,68384,202376,-3792,0,43200,129600,0,39603,893),
(25192,1,125826,189112,-3344,0,43200,129600,0,56386,1296),
(25198,1,102656,157424,-3735,0,43200,129600,0,483261,2639),
(25199,1,108096,157408,-3688,0,43200,129600,0,214875,2707),
(25202,1,119760,157392,-3744,0,43200,129600,0,248996,2777),
(25205,1,123808,153408,-3671,0,43200,129600,0,220403,3274),
(25208,1,73806,201274,-3924,0,43200,129600,0,50445,1722),
(25211,1,76272,192484,-3808,0,43200,129600,0,43053,1975),
(25214,1,111853,209177,-3687,0,43200,129600,0,50445,2368),
(25217,1,89782,105028,-3340,0,43200,129600,0,71339,1722),
(25220,1,113414,16654,-2172,0,43200,129600,0,247349,3274),
(25223,1,42247,152017,-2894,0,43200,129600,0,41308,1237),
(25226,1,103356,-4392,-3536,0,43200,129600,0,193664,2502),
(25229,1,137542,-20120,-3740,0,43200,129600,0,501018,3420),
(25230,1,66614,46216,-3948,0,43200,129600,0,87272,2169),
(25233,1,113146,17068,-2936,0,43200,129600,0,209541,3643),
(25234,1,119474,110944,-3196,0,43200,129600,0,201006,2707),
(25235,1,115280,-63048,-3372,0,43200,129600,0,245570,3202),
(25238,1,157318,-57560,-3240,0,43200,129600,0,102733,2846),
(25241,1,165834,87576,-2464,0,43200,129600,0,153521,2639),
(25244,1,187258,45680,-5928,0,43200,129600,0,438385,3420),
(25245,1,171762,55028,-5992,0,43200,129600,0,206546,3643),
(25248,1,176854,-8700,-3500,0,43200,129600,0,399054,3274),
(25249,1,147252,-21592,-3560,0,43200,129600,0,219192,3420),
(25252,1,192346,21528,-3648,0,43200,129600,0,211425,3058),
(25255,1,170038,-26236,-3824,0,43200,129600,0,373296,2707),
(25256,1,170088,42248,-4912,0,43200,129600,0,94188,2368),
(25259,1,42050,208107,-3752,0,43200,129600,0,307043,2039),
(25260,1,92552,18716,-3696,0,43200,129600,0,112383,1722),
(25263,1,144242,-28588,-2072,0,43200,129600,0,190791,2846),
(25266,1,188502,12836,-2796,0,43200,129600,0,250509,3420),
(25269,1,123450,-24570,-3604,0,43200,129600,0,211425,3058),
(25272,1,48705,127446,-3761,0,43200,129600,0,60567,1415),
(25276,1,154088,-14116,-3736,0,43200,129600,0,501018,3420),
(25277,1,53850,179973,-5013,0,43200,129600,0,142678,1722),
(25280,1,84881,88422,-5155,0,43200,129600,0,330662,2039),
(25281,1,150763,87529,-5476,0,43200,129600,0,422851,3058),
(25282,1,179311,-7632,-4896,0,43200,129600,0,501018,3420),
(25293,1,134382,-116328,-1300,0,43200,129600,0,206546,3718),
(25299,1,147606,-74912,-4964,0,43200,129600,0,111981,3718),
(25302,1,145592,-82264,-6064,0,43200,129600,0,112730,3718),
(25305,1,144456,-85488,-6312,0,43200,129600,0,225198,3718),
(25309,1,114988,-40008,-2540,0,43200,129600,0,112599,3718),
(25312,1,108662,-36964,-1248,0,43200,129600,0,111981,3718),
(25315,1,105676,-43808,-1840,0,43200,129600,0,112730,3718),
(25319,1,184816,-106872,-6384,0,43200,129600,0,225198,3718),
(25322,1,93280,-75632,-1984,0,43200,129600,0,112599,3718),
(25325,1,91602,-86257,-2715,0,43200,129600,0,257725,3718),
-- (25328,1,59331,-42403,-3003,0,7200,10800,0,232323,3718), -- should be event spawn ???
-- (25339,1,191544,-85575,-7184,-33016,60,60,0,211425,3718), -- should be event spawn ???
-- (25339,1,189801,-88965,-7184,-33016,60,60,0,243663,3718), -- should be event spawn ???
-- (25339,1,173193,-76299,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
-- (25339,1,175610,-72453,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
-- (25342,1,191544,-85575,-7184,-33016,60,60,0,96646,3718), -- should be event spawn ???
-- (25342,1,189801,-88965,-7184,-33016,60,60,0,96646,3718), -- should be event spawn ???
-- (25342,1,173193,-76299,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
-- (25342,1,175610,-72453,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
-- (25346,1,191544,-85575,-7184,-33016,60,60,0,96646,3718), -- should be event spawn ???
-- (25346,1,189801,-88965,-7184,-33016,60,60,0,96646,3718), -- should be event spawn ???
-- (25346,1,173193,-76299,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
-- (25346,1,175610,-72453,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
-- (25349,1,191544,-85575,-7184,-33016,60,60,0,96646,3718), -- should be event spawn ???
-- (25349,1,189801,-88965,-7184,-33016,60,60,0,96646,3718), -- should be event spawn ???
-- (25349,1,173193,-76299,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
-- (25349,1,175610,-72453,-7184,-15992,60,60,0,96646,3718), -- should be event spawn ???
(25352,1,-16870,174032,-3584,0,43200,129600,0,28471,3718),
(25354,1,-16494,183800,-3964,0,43200,129600,0,41308,3718),
(25357,1,-4056,112216,-3632,0,43200,129600,0,18330,3718),
(25360,1,28864,178924,-3728,0,43200,129600,0,23592,3718),
(25362,1,-56268,186236,-3456,0,43200,129600,0,20324,3718),
(25365,1,-62536,189304,-3760,0,43200,129600,0,47184,3718),
(25366,1,-62914,178760,-3688,0,43200,129600,0,20324,3718),
(25369,1,-45896,110708,-3880,0,43200,129600,0,22463,3718),
(25372,1,47859,243224,-6762,0,43200,129600,0,34766,3718),
(25373,1,9430,76692,-3852,0,43200,129600,0,18330,3718),
(25375,1,22302,80152,-3272,0,43200,129600,0,17383,3718),
(25378,1,-54420,83232,-3648,0,43200,129600,0,17383,3718),
(25380,1,-47960,51042,-5959,0,43200,129600,0,18330,3718),
(25383,1,51372,153158,-3608,0,43200,129600,0,33945,3718),
(25385,1,53370,142749,-3932,0,43200,129600,0,36903,3718),
(25388,1,39813,101470,-1390,0,43200,129600,0,35407,3718),
(25391,1,44804,119953,-2758,0,43200,129600,0,65044,3718),
(25392,1,29614,106484,-3772,0,43200,129600,0,31134,3718),
(25394,1,101046,199276,-3780,0,43200,129600,0,80010,3718),
(25395,1,21360,109027,-9018,0,43200,129600,0,51869,3718),
(25398,1,8424,188184,-3868,0,43200,129600,0,35407,3718),
(25401,1,117494,101996,-3740,0,43200,129600,0,31134,3718),
(25404,1,35910,190808,-3124,0,43200,129600,0,32522,3718),
(25407,1,114932,111828,-3080,0,43200,129600,0,80732,3718),
(25410,1,72096,124692,-3720,0,43200,129600,0,50445,3718),
(25412,1,81954,112572,-3224,0,43200,129600,0,55512,3718),
(25415,1,128208,137880,-3564,0,43200,129600,0,35407,3718),
(25418,1,62510,7440,-3584,0,43200,129600,0,50083,3718),
(25420,1,42200,22716,-5008,0,43200,129600,0,66930,3718),
(25423,1,113036,45688,-4696,0,43200,129600,0,84968,3718),
(25426,1,-18736,-102168,-2180,0,43200,129600,0,22463,3718),
(25429,1,171756,-215672,-3664,0,43200,129600,0,22463,3718),
(25431,1,79226,17696,-5524,0,43200,129600,0,50083,3718),
(25434,1,103658,-17984,-2036,0,43200,129600,0,70856,3718),
(25437,1,66834,63212,-3844,0,43200,129600,0,103738,3718),
(25438,1,123530,93488,-2464,0,43200,129600,0,50083,3718),
(25441,1,111390,82368,-2952,0,43200,129600,0,51869,3718),
(25444,1,113140,17056,-4420,0,43200,129600,0,86145,3718),
(25447,1,113158,17052,-1448,0,43200,129600,0,91375,3718),
(25450,1,113406,14544,9528,0,43200,129600,0,254211,3718),
(25453,1,156758,-7000,-4304,0,43200,129600,0,196324,3718),
(25456,1,133426,86544,-3696,0,43200,129600,0,59249,3718),
(25460,1,150260,67156,-3804,0,43200,129600,0,63062,3718),
(25463,1,166056,67440,-3348,0,43200,129600,0,72830,3718),
(25467,1,185908,61084,-4200,0,43200,129600,0,85133,3718),
(25470,1,186688,56016,-4680,0,43200,129600,0,87120,3718),
(25473,1,174466,29532,-3872,0,43200,129600,0,64995,3718),
(25475,1,183042,24232,-3204,0,43200,129600,0,70856,3718),
(25478,1,167592,27868,-3756,0,43200,129600,0,86145,3718),
(25481,1,52950,205080,-3788,0,43200,129600,0,66938,3718),
(25484,1,42874,219668,-3808,0,43200,129600,0,61148,3718),
(25487,1,82874,182768,-3740,0,43200,129600,0,43238,3718),
(25490,1,86544,216048,-3776,0,43200,129600,0,43238,3718),
(25493,1,82145,251452,-10634,0,43200,129600,0,70856,3718),
(25496,1,80989,257537,-9378,0,43200,129600,0,64995,3718),
(25498,1,126688,173368,-3188,0,43200,129600,0,51869,3718);
-- (25501,1,48296,-106689,-1584,0,43200,129600,0,127782,9999), -- stats to be done
-- (25504,1,122635,-141065,-1498,0,43200,129600,0,206753,9999), -- stats to be done
-- (25506,1,127823,-160493,-1228,0,43200,129600,0,184670,9999), -- stats to be done
-- (25509,1,74336,-101733,-920,0,43200,129600,0,418874,9999), -- stats to be done
-- (25512,1,x,y,z,0,43200,129600,0,804638,9999), -- no coords yet & stats to be done
-- (25513,1,x,y,z,0,43200,129600,0,350000,9999), -- no coords yet & stats to be done
-- (25514,1,x,y,z,0,43200,129600,0,714778,9999), -- no coords yet & stats to be done
-- (25517,1,x,y,z,0,43200,129600,0,1069643,9999), -- no coords yet & stats to be done
-- (25523,1,x,y,z,0,43200,129600,0,1848045,9999), -- no coords yet & stats to be done
-- (25524,1,x,y,z,0,43200,129600,0,956490,9999), -- no coords yet & stats to be done
-- (29056,1,x,y,z,0,43200,129600,0,350000,9999), -- no coords yet & stats to be done
-- (29060,1,x,y,z,0,43200,129600,0,350000,9999), -- no coords yet & stats to be done
-- (29062,1,x,y,z,0,43200,129600,0,400000,9999); -- no coords yet & stats to be done
