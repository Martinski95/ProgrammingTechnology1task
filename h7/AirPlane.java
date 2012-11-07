"""Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Трябва да се направи програма, която подрежда пътниците в самолет според това как идват (на групи по 1 2 или 3-ма) в 6 колони
разделени на 2.
"""




import java.util.Random;
import java.io.IOException;
public class AirPlane {

	public void printSeats(int[][] seat) {		
		for (int r=0; r<27; r++) {
			for (int c=0; c<6; c++) {
				System.out.print(" " + seat[c][r]);
				if(c==2) System.out.print("  ");
			}
			System.out.println("");
		}
		System.out.println("*******************************************************************");			
		try {
			int press = System.in.read();
			press = System.in.read();
		}
		catch(IOException e) {
			System.out.println("Error");
		}
	}

	public int generatePassengers() {
		return (1 + (int)Math.round(Math.random() * 2));
	}
	
	public void addPassengers(int currPassengers, int[][] seat) {
		int totalPassengers = 0;
		int maxPassengers = seat.length;
		boolean isTaken = false;
		System.out.println("Last passangers = " + currPassengers);
		for(int r = 0; r < 27; r++) {
			for(int c = 0; c < 6; c++) {
				if(currPassengers == 1) {
					if(seat[c][r] == 0) {
						seat[c][r] = 1;
						isTaken = true;
						break;
					}
				}else if(currPassengers == 2) {
					if((c != 2) && (c != 5) && (seat[c][r] == 0) && (seat[c+1][r] == 0)) {
						seat[c][r] = 2;
						seat[c+1][r] = 2;
						isTaken = true;
						break;
					}
				}else if(currPassengers == 3) {
					if( ((c == 0) || (c == 3)) && (seat[c][r] == 0) && (seat[c+1][r] == 0) && (seat[c+2][r] == 0)) {
						seat[c][r] = 3;
						seat[c+1][r] = 3;
						seat[c+2][r] = 3;
						isTaken = true;
						break;
					}
				}
			}
			if(isTaken)
				break;
		}
		if(isTaken) {
			totalPassengers += currPassengers;
		}
	}
	
	public boolean isFull(int[][] seat) {
		int takenSeatsCount = 0;
		for(int c = 0; c < 6; c++) {
			for(int r = 0; r < 27; r++) {
				if(seat[c][r] != 0) {
					takenSeatsCount++;
				}
			}
		}
		if(takenSeatsCount >= 6*27)
			return true;
		else
			return false;
	}
	
	public static void main(String[] args){
		int[][] seats = new int[6][27];
		AirPlane plane = new AirPlane();
		int currentPassengers = 0;

		while(!plane.isFull(seats)) {
			currentPassengers = plane.generatePassengers();
			plane.addPassengers(currentPassengers, seats);
			plane.printSeats(seats);
		}
	}
}
