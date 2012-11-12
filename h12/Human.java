public class Human {

	public enum Gender {
		MALE,
		FEMALE,
		_NOGENDER_
	}; 
	
	Gender gender;
	public String name;
	public boolean isSitting;
	
	public String[] maleNames =   {"[Georgi  ]", "[Stefan  ]", "[Petur   ]", "[Ivan    ]", "[Martin  ]", "[Nikolai ]", "[Anton   ]", "[Asen    ]", "[Stoqn   ]", "[Tihomir ]", "[Krasimir]", "[Kristiqn]", "[Samuil  ]", "[Dimitur ]", "[Kiril   ]"};
	public String[] femaleNames = {"[Ivana   ]", "[Stefka  ]", "[Iliqna  ]", "[Elena   ]", "[Mariq   ]", "[Snejinka]", "[Ani     ]", "[Polina  ]", "[Kristin ]", "[Diana   ]", "[Lilia   ]", "[Alisa   ]", "[Margi   ]", "[Sonq    ]", "[Gabriela]"};
									
	public Human() {
		gender = gender ._NOGENDER_;
		name = "[NO  NAME]";
		isSitting = false;
	}
	
	public Gender generateGender() { 
		int gender = ((int)Math.round(Math.random()));
		if(gender == 0) {
			return Gender.MALE;
		}
		else if(gender == 1) {
			return Gender.FEMALE;
		}else {
			return Gender._NOGENDER_;
		}
	}
	
	public String generateName(Gender gend) {
		if(gend == Gender.FEMALE) {
			return femaleNames[((int)Math.round(Math.random() * 13))];
		}
		else {
			return maleNames[((int)Math.round(Math.random() * 13))];
		}
	}
	
	public Gender getGender() {
		return gender;
	}

	public void setName(Gender gend) {
		name = generateName(gend);
	}
	
	public void setGender(Gender gend) {
		gender = gend;
	}
	
	public void remove() {
		 gender = null;
		 name= null;
		 isSitting = false;
	}
}