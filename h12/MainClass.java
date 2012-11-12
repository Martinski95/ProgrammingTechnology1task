public class MainClass {

	
	
	public static void main(String[] args) {
		Airplane Plane = new Airplane();
		
		while(!Plane.isFull()) {
			Plane.add(Plane.generateGroup());
			Plane.printSeats();
		}	
		System.out.println(Plane.getMales());
		Plane.clear();
		Plane.printSeats();
	}
}
