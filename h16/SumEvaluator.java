package org.elsys.eval;

import java.util.ArrayList;

public class SumEvaluator implements IEvaluator {
	
	ArrayList<Double> list;
	
	public SumEvaluator() {
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
		return sum;
	}

}
