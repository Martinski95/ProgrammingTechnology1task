package org.elsys.ballsAndBoxes;

public class MainClass {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Box box = new Box(10);
		Ball b1 = new Ball();
		Ball b2 = new Ball();
		Ball b3 = new Ball();
		Ball b4 = new Ball();
		box.addBall(b1);
		box.addBall(b2);
		box.addBall(b3);
		System.out.println("Box size : " + box.size());
		System.out.println("Box capacity : " + box.getCapacity());
		
		box.addBall(b3);
		box.addBall(b3);
		System.out.println("Box size : " + box.size());
		System.out.println("Box capacity : " + box.getCapacity());
		
		box.addBall(b4);
		System.out.println("Box size : " + box.size());
		System.out.println("Box capacity : " + box.getCapacity());
		
		
		box.remove(b1);
		
		System.out.println("Box size : " + box.size());
		System.out.println("Box capacity : " + box.getCapacity());
	}

}
