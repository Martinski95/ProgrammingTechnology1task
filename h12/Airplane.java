import java.io.IOException;
import java.util.ArrayList;

public class Airplane {
	public Human[][] seats;
	
	public Airplane() {
		seats = new Human[6][27];
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				seats[c][r] = new Human();
					seats[c][r].gender = seats[c][r].gender._NOGENDER_;
					seats[c][r].name = "[NO  NAME]";
					seats[c][r].isSitting = false;
			}
		}
	}
	
	public ArrayList<Human> generateGroup() {
		ArrayList<Human> group = new ArrayList<Human>();
		int peopleInGroup = (1 + (int)Math.round(Math.random() * 2));
		
		for(int i = 0; i < peopleInGroup; i++) {
			Human h1 = new Human();
			h1.setGender(h1.generateGender());
			h1.setName(h1.gender);
			h1.isSitting = false;
			group.add(h1);
		}
		return group;
	}
	
	public void add(ArrayList<Human> group) {
		int currPassengers = group.size();
		boolean isTaken = false;
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				if(currPassengers == 1) {
					if(seats[c][r].isSitting == false) {
						seats[c][r].gender = group.get(0).gender;	
						seats[c][r].name = group.get(0).name;
						seats[c][r].isSitting = true;
						isTaken = true;
						break;
					}
				}
				else if(currPassengers == 2) {
					if(c+1 > 5) {
						break;
					}
					if( (c != 2) && (c != 5) && (seats[c][r].isSitting == false) && (seats[c+1][r].isSitting == false) ) {
						seats[c][r].gender = group.get(0).gender;
						seats[c][r].name = group.get(0).name;
						seats[c][r].isSitting = true;
						seats[c+1][r].gender = group.get(1).gender;
						seats[c+1][r].name = group.get(1).name;
						seats[c+1][r].isSitting = true;
						isTaken = true;
						break;
					}
				}
				else if(currPassengers == 3 && c < 4) {
					if(c+2 > 5) {
						break;
					}
					if( ( (c == 0) || (c == 3) ) && (seats[c][r].isSitting == false) && (seats[c+1][r].isSitting == false) && (seats[c+2][r].isSitting == false) ) {
						seats[c][r].gender = group.get(0).gender;
						seats[c][r].name = group.get(0).name;
						seats[c][r].isSitting = true;
						seats[c+1][r].gender = group.get(1).gender;
						seats[c+1][r].name = group.get(1).name;
						seats[c+1][r].isSitting = true;
						seats[c+2][r].gender = group.get(2).gender;
						seats[c+2][r].name = group.get(2).name;
						seats[c+2][r].isSitting = true;
						isTaken = true;
						break;
					}
				}
			}
			if(isTaken) {
				break;
			}
		}
	}
	
	public void remove(Human h) {
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				if((seats[c][r].gender == h.gender) && (seats[c][r].name == h.name) && (h.isSitting)) {
					seats[c][r].remove();
				}
			}
		}
	}
	
	public void clear() {
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				seats[c][r] = null;
			}
		}
	}
	
	public int getCapacity() {
		int capacity = 0;
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				if(seats[c][r].isSitting == false) {
					capacity++;
				}
			}
		}
		return capacity; 
	}
	
	public int getMales() {
		int males = 0;
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				if(seats[c][r].gender == Human.Gender.MALE) {
					males++;
				}
			}
		}
		return males;
	}
	
	public int getFemales() {
		int females = 0;
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				if(seats[c][r].gender == Human.Gender.FEMALE) {
					females++;
				}
			}
		}
		return females;
	}
	
	public boolean isFull() {
		int places = 0;
		for(int r = 0;r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				if(seats[c][r].isSitting == true) {
					places++;
				}
			}
		}
		if(places < 6*27) {
			return false;
		}else {
			return true;
		}
	}
	
	public void printSeats() {
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {

				if(seats[c][r] != null) {
					System.out.print("  "+ seats[c][r].name);
				}else {
					System.out.print("  " + "[EMPTY   ]");
				}
				if(c == 2) System.out.print("   | ");
			}
			System.out.println("");
		}
		System.out.println("*****************************************************************************");			
		try {																		   
			int press = System.in.read();
			press = System.in.read();
		}
		catch(IOException e) {
			System.out.println("Error");
		}
	}
}
