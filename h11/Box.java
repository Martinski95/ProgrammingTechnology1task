package org.elsys.ballsAndBoxes;
import java.util.LinkedList;

public class Box {
	int maxSize;
	LinkedList<Ball> boxList = new LinkedList<Ball>();
	Box(int _maxSize) {
		maxSize = _maxSize;
	}
	public void addBall(Ball b) {
		if(!boxList.contains(b)) {
			boxList.addLast(b);
		}
	}
	
	public void remove(Ball b) {
		boxList.remove(b);
	}
	
	public int getCapacity() {
		return maxSize - boxList.size();
	}
	
	public int size() {
		return boxList.size();
	}
	
	public void clear() {
		boxList.clear();
	}
	
	public boolean contains(Ball b) {
		return boxList.contains(b);
	}
}
