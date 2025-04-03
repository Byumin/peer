*교사버전 

RECODE w1_T_emotionvalid4 w1_T_emotionvalid6 w1_T_emotionvalid7 w1_T_emotionvalid8 
(1=5) (2=4) (3=3) (4=2) (5=1) INTO w1_T_emotionvalid4_r w1_T_emotionvalid6_r w1_T_emotionvalid7_r w1_T_emotionvalid8_r.

EXECUTE.


*T_SDMS status Alpha  

RELIABILITY
  /VARIABLES=w1_T_self_status1 w1_T_self_status2 w1_T_self_status3 w1_T_self_status4 w1_T_self_status5 w1_T_self_status6
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.
  
*T_SDMS network isolation Alpha  

RELIABILITY
  /VARIABLES=w1_T_self_network_isolate1 w1_T_self_network_isolate2 w1_T_self_network_isolate3 w1_T_self_network_isolate4
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.
  
*T_SDMS network problem Alpha  

RELIABILITY
  /VARIABLES=w1_T_self_network_problem1 w1_T_self_network_problem2 w1_T_self_network_problem3
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.
  
*T_SDMS manage aggression Alpha  

RELIABILITY
  /VARIABLES=w1_T_self_manage_aggression1 w1_T_self_manage_aggression2 w1_T_self_manage_aggression3 w1_T_self_manage_aggression4 w1_T_self_manage_aggression5
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.
  
*T_SDMS manage positive Alpha  

RELIABILITY
  /VARIABLES=w1_T_self_manage_positive1 w1_T_self_manage_positive2 w1_T_self_manage_positive3 w1_T_self_manage_positive4 w1_T_self_manage_positive5
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Teacher self efficacy peer Alpha  

RELIABILITY
  /VARIABLES=w1_T_self_efficacy_peer1 w1_T_self_efficacy_peer2 w1_T_self_efficacy_peer3 w1_T_self_efficacy_peer4 w1_T_self_efficacy_peer5 w1_T_self_efficacy_peer6 w1_T_self_efficacy_peer7
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.
  
*Teacher self efficacy manage Alpha  

RELIABILITY
  /VARIABLES=w1_T_self_efficacy_manage1 w1_T_self_efficacy_manage2 w1_T_self_efficacy_manage3 w1_T_self_efficacy_manage4
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Teacher exhaustion Alpha  

RELIABILITY
  /VARIABLES=w1_T_exhaust1 w1_T_exhaust2 w1_T_exhaust3 w1_T_exhaust4 w1_T_exhaust5 w1_T_exhaust6 w1_T_exhaust7 w1_T_exhaust8 w1_T_exhaust9 w1_T_exhaust10 w1_T_exhaust11 w1_T_exhaust12
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Teacher Emotional validation Alpha   

RELIABILITY
  /VARIABLES=w1_T_emotionvalid1 w1_T_emotionvalid2 w1_T_emotionvalid3 w1_T_emotionvalid4_r w1_T_emotionvalid5 w1_T_emotionvalid6_r w1_T_emotionvalid7_r w1_T_emotionvalid8_r w1_T_emotionvalid9 w1_T_emotionvalid10
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*T_SDMS status Mean

COMPUTE w1_t_status_mean=MEAN(w1_T_self_status1,w1_T_self_status2,w1_T_self_status3,w1_T_self_status4,w1_T_self_status5,w1_T_self_status6). 
EXECUTE. 

*T_SDMS network isolation Mean

COMPUTE w1_t_networkisolate_mean=MEAN(w1_T_self_network_isolate1,w1_T_self_network_isolate2,w1_T_self_network_isolate3,w1_T_self_network_isolate4). 
EXECUTE. 

*T_SDMS network problem Mean

COMPUTE w1_t_networkproblem_mean=MEAN(w1_T_self_network_problem1,w1_T_self_network_problem2,w1_T_self_network_problem3). 
EXECUTE. 

*T_SDMS manage aggression Mean

COMPUTE w1_t_manageaggression_mean=MEAN(w1_T_self_manage_aggression1,w1_T_self_manage_aggression2,w1_T_self_manage_aggression3,w1_T_self_manage_aggression4,w1_T_self_manage_aggression5). 
EXECUTE. 

*T_SDMS manage positive Mean

COMPUTE w1_t_managepositive_mean=MEAN(w1_T_self_manage_positive1,w1_T_self_manage_positive2,w1_T_self_manage_positive3,w1_T_self_manage_positive4,w1_T_self_manage_positive5). 
EXECUTE. 

*Teacher self efficacy peer Mean

COMPUTE w1_t_selfefficacypeer_mean=MEAN(w1_T_self_efficacy_peer1,w1_T_self_efficacy_peer2,w1_T_self_efficacy_peer3,w1_T_self_efficacy_peer4,w1_T_self_efficacy_peer5,w1_T_self_efficacy_peer6,w1_T_self_efficacy_peer7). 
EXECUTE.

*Teacher self efficacy manage Mean

COMPUTE w1_t_selfefficacymanage_mean=MEAN(w1_T_self_efficacy_manage1,w1_T_self_efficacy_manage2,w1_T_self_efficacy_manage3,w1_T_self_efficacy_manage4). 
EXECUTE.

*Teacher exhaustion Mean

COMPUTE w1_t_exhaustion_mean=MEAN(w1_T_exhaust1,w1_T_exhaust2,w1_T_exhaust3,w1_T_exhaust4,w1_T_exhaust5,w1_T_exhaust6,w1_T_exhaust7,w1_T_exhaust8,w1_T_exhaust9,w1_T_exhaust10,w1_T_exhaust11,w1_T_exhaust12). 
EXECUTE.

*T_Emotional validation Mean

COMPUTE w1_T_emotionvalid_mean=MEAN(w1_T_emotionvalid1,w1_T_emotionvalid2,w1_T_emotionvalid3,w1_T_emotionvalid4_r,w1_T_emotionvalid5,w1_T_emotionvalid6_r,w1_T_emotionvalid7_r,w1_T_emotionvalid8_r,w1_T_emotionvalid9,w1_T_emotionvalid10). 
EXECUTE. 

