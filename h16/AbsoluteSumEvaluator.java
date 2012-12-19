package org.elsys.eval;

public class AbsoluteSumEvaluator extends SumEvaluator implements IEvaluator {

	public AbsoluteSumEvaluator() {
		super();
	}
	
	@Override
	public void add(double d) {
		super.add(d);
	}

	@Override
	public Double evaluate() {
		double sum = 0;
		for(int i = 0; i < list.size(); i++) {
			sum += Math.abs(list.get(i));
		}
		return sum;
	}

}
