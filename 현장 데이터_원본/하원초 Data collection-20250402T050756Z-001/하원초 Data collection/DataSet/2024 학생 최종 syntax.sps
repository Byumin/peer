*RECODE growth mindset, emotional validation

RECODE w1_growth1 w1_growth2 w1_growth3 w1_growth4 w1_emotionvalid_P4 w1_emotionvalid_P6 w1_emotionvalid_P7 w1_emotionvalid_P8 w1_emotionvalid_T4 w1_emotionvalid_T6 w1_emotionvalid_T7 w1_emotionvalid_T8 (1=5) (2=4) (3=3) (4=2) (5=1) INTO w1_growth1_r w1_growth2_r w1_growth3_r w1_growth4_r w1_emotionvalid_P4_r w1_emotionvalid_P6_r w1_emotionvalid_P7_r w1_emotionvalid_P8_r w1_emotionvalid_T4_r w1_emotionvalid_T6_r w1_emotionvalid_T7_r w1_emotionvalid_T8_r.
EXECUTE.

*Relational Aggression Alpha

RELIABILITY
  /VARIABLES=w1_ra1 w1_ra2
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
/SUMMARY=TOTAL.

*Prosocial Alpha

RELIABILITY
 /VARIABLES=w1_pro1 w1_pro2
 /SCALE('ALL VARIABLES') ALL
 /MODEL=ALPHA
 /SUMMARY=TOTAL.

*Growth Mindset Alpha  

RELIABILITY
  /VARIABLES=w1_growth1_r w1_growth2_r w1_growth3_r w1_growth4_r
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Behavioral Engagement Alpha  

RELIABILITY
  /VARIABLES=w1_behavioraleng1 w1_behavioraleng2 w1_behavioraleng3 w1_behavioraleng4 w1_behavioraleng5
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Emotional Engagement Alpha  

RELIABILITY
  /VARIABLES=w1_emotionaleng1 w1_emotionaleng2 w1_emotionaleng3 w1_emotionaleng4 w1_emotionaleng5
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
/SUMMARY=TOTAL.

*CPCQ Alpha
*CPCQ comfort

RELIABILITY
  /VARIABLES=w1_comfort1 w1_comfort2 w1_comfort3 w1_comfort4 
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*CPCQ cooperation

RELIABILITY
  /VARIABLES=w1_cooperation1 w1_cooperation2 w1_cooperation3 w1_cooperation4 
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*CPCQ conflict

RELIABILITY
  /VARIABLES=w1_conflict1 w1_conflict2 w1_conflict3 w1_conflict4 
  /SCALE('ALL VARIABLES') ALL 
 /MODEL=ALPHA
  /SUMMARY=TOTAL.

*CPCQ cohesion

RELIABILITY
  /VARIABLES=w1_cohesion1 w1_cohesion2 w1_cohesion3 w1_cohesion4 
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*CPCQ isolation

RELIABILITY
  /VARIABLES=w1_isolation1 w1_isolation2 w1_isolation3 w1_isolation4
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Popularity Strive Alpha  

RELIABILITY
  /VARIABLES=w1_popstrive1 w1_popstrive2 w1_popstrive3
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.
  
*Popularity Fear Alpha   

RELIABILITY
  /VARIABLES=w1_popfear1 w1_popfear2 w1_popfear3
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Cooperation Alpha  

RELIABILITY
  /VARIABLES=w1_coop1 w1_coop2 w1_coop3
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Competitive Alpha  

RELIABILITY
  /VARIABLES=w1_compete1 w1_compete2 w1_compete3 w1_compete4
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Social Mistrust Alpha  

RELIABILITY
  /VARIABLES=w1_peer_mistrust1 w1_peer_mistrust2 w1_peer_mistrust3 w1_peer_mistrust4 w1_peer_mistrust5 w1_peer_mistrust6 w1_peer_mistrust7 w1_peer_mistrust8 w1_peer_mistrust9 w1_peer_mistrust10
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Co-rumination Alpha  

RELIABILITY
  /VARIABLES=w1_corum6 w1_corum9 w1_corum11 w1_corum12 w1_corum15 w1_corum16 w1_corum17 w1_corum18 w1_corum24
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Emotional validation Parent Alpha   

RELIABILITY
  /VARIABLES=w1_emotionvalid_P1 w1_emotionvalid_P2 w1_emotionvalid_P3 w1_emotionvalid_P4_r w1_emotionvalid_P5 w1_emotionvalid_P6_r w1_emotionvalid_P7_r w1_emotionvalid_P8_r w1_emotionvalid_P9 w1_emotionvalid_P10
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Emotional validation Teacher Alpha   

RELIABILITY
  /VARIABLES=w1_emotionvalid_T1 w1_emotionvalid_T2 w1_emotionvalid_T3 w1_emotionvalid_T4_r w1_emotionvalid_T5 w1_emotionvalid_T6_r w1_emotionvalid_T7_r w1_emotionvalid_T8_r w1_emotionvalid_T9 w1_emotionvalid_T10
  /SCALE('ALL VARIABLES') ALL
  /MODEL=ALPHA
  /SUMMARY=TOTAL.

*Relational Aggression Mean

COMPUTE w1_ra_mean=MEAN(w1_ra1,w1_ra2). 
EXECUTE. 

*Prosocial Mean

COMPUTE w1_pro_mean=MEAN(w1_pro1,w1_pro2). 
EXECUTE. 


*Growth Mindset Mean

COMPUTE w1_growth_mean=MEAN(w1_growth1_r,w1_growth2_r,w1_growth3_r,w1_growth4_r). 
EXECUTE. 

*Behavioral Engagement Mean

COMPUTE w1_behavioralengagement_mean=MEAN(w1_behavioraleng1,w1_behavioraleng2,w1_behavioraleng3,w1_behavioraleng4,w1_behavioraleng5). 
EXECUTE.

*Emotional Engagement Mean

COMPUTE w1_emotionalengagement_mean=MEAN(w1_emotionaleng1,w1_emotionaleng2,w1_emotionaleng3,w1_emotionaleng4,w1_emotionaleng5). 
EXECUTE.

*CPCQ Mean
*CPCQ comfort mean

COMPUTE w1_comfort_mean=MEAN(w1_comfort1,w1_comfort2,w1_comfort3,w1_comfort4). 
EXECUTE. 

*CPCQ cooperation mean

COMPUTE w1_cooperation_mean=MEAN(w1_cooperation1,w1_cooperation2,w1_cooperation3,w1_cooperation4). 
EXECUTE. 

*CPCQ conflict mean

COMPUTE w1_conflict_mean=MEAN(w1_conflict1,w1_conflict2,w1_conflict3,w1_conflict4). 
EXECUTE. 

*CPCQ cohesion mean

COMPUTE w1_cohesion_mean=MEAN(w1_cohesion1,w1_cohesion2,w1_cohesion3,w1_cohesion4). 
EXECUTE. 

*CPCQ isolation mean

COMPUTE w1_isolation_mean=MEAN(w1_isolation1,w1_isolation2,w1_isolation3,w1_isolation4). 
EXECUTE. 

*Popularity strive mean

COMPUTE w1_popstrive_mean=MEAN(w1_popstrive1,w1_popstrive2,w1_popstrive3). 
EXECUTE. 

*Popularity fear mean

COMPUTE w1_popfear_mean=MEAN(w1_popfear1,w1_popfear2,w1_popfear3). 
EXECUTE. 

*Cooperation Mean

COMPUTE w1_coop_mean=MEAN(w1_coop1,w1_coop2,w1_coop3). 
EXECUTE. 

*Competitive Mean

COMPUTE w1_competitive_mean=MEAN(w1_compete1,w1_compete2,w1_compete3,w1_compete4). 
EXECUTE. 

*Social Mistrust Mean

COMPUTE w1_peermistrust_mean=MEAN(w1_peer_mistrust1,w1_peer_mistrust2,w1_peer_mistrust3,w1_peer_mistrust4,w1_peer_mistrust5,w1_peer_mistrust6,w1_peer_mistrust7,w1_peer_mistrust8,w1_peer_mistrust9,w1_peer_mistrust10). 
EXECUTE.

*Co-rumination Mean

COMPUTE w1_corumination_mean=MEAN(w1_corum6,w1_corum9,w1_corum11,w1_corum12,w1_corum15,w1_corum16,w1_corum17,w1_corum18,w1_corum24). 
EXECUTE.

*Emotional validation_P Mean

COMPUTE w1_emotionvalid_p_mean=MEAN(w1_emotionvalid_P1,w1_emotionvalid_P2,w1_emotionvalid_P3,w1_emotionvalid_P4_r,w1_emotionvalid_P5,w1_emotionvalid_P6_r,w1_emotionvalid_P7_r,w1_emotionvalid_P8_r,w1_emotionvalid_P9,w1_emotionvalid_P10). 
EXECUTE. 

*Emotional validation_T Mean

COMPUTE w1_emotionvalid_t_mean=MEAN(w1_emotionvalid_T1,w1_emotionvalid_T2,w1_emotionvalid_T3,w1_emotionvalid_T4_r,w1_emotionvalid_T5,w1_emotionvalid_T6_r,w1_emotionvalid_T7_r,w1_emotionvalid_T8_r,w1_emotionvalid_T9,w1_emotionvalid_T10). 
EXECUTE. 
