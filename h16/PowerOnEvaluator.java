package org.elsys.eval;

import java.util.ArrayList;

public class PowerOnEvaluator implements IEvaluator {
	
	public ArrayList<Double> list;
	public double step = 0;
	
	public PowerOnEvaluator() {
		list = new ArrayList<Double>();
		step = 2;
	}
	
	public PowerOnEvaluator(double power) {
		list = new ArrayList<Double>();
		step = power;
	}
	@Override
	public void add(double d) {
		list.add(d);
	}

	@Override
	public Double evaluate() {
		for(int i = 0; i < list.size(); i++) {
			double pow = Math.pow(list.get(i), step);
			list.set(i, pow);
			System.out.println("Element " + i + " = " + list.get(i));
		}
		return null;
	}

}
