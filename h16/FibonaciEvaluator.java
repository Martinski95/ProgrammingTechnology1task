package org.elsys.eval;

import java.util.ArrayList;

public class FibonaciEvaluator implements IEvaluator {

	ArrayList<Double> list;
	
	public FibonaciEvaluator() {
		list = new ArrayList<Double>();
	}
	
	@Override
	public void add(double d) {
		list.add(d);
	}

	@Override
	public Double evaluate() {
		double sum = 0;
		for(int i = 0; i < list.size(); i++) {
			sum += list.get(i);
		}
		int first = 1;
		int second = 1;
		int next = 0;
		int diff1 = 0;
		int diff2 = 0;
		int lastFib = 0;
		while(true) {
			
			next = first + second;
			first = second;
			second = next;
			
			if(Math.abs(sum) < next) {
				diff1 = (int) (sum - lastFib);
				diff2 = (int) (sum - next);
				if(Math.abs(diff1) < Math.abs(diff2)) {
					return (double) lastFib;
				} else if(Math.abs(diff1) > Math.abs(diff2)){
					return (double) next;
				} else {
					return (double) 0;
				}
			}
			
			lastFib = next;
		}
		
	}

}
