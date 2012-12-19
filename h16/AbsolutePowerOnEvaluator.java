package org.elsys.eval;

public class AbsolutePowerOnEvaluator extends PowerOnEvaluator implements IEvaluator {

	public AbsolutePowerOnEvaluator() {
		super();
	}
	
	public AbsolutePowerOnEvaluator(double power) {
		super(power);
	}
	
	@Override
	public void add(double d) {
		super.add(Math.round(d));
	}

	@Override
	public Double evaluate() {
		super.evaluate();
		return null;
	}

}
