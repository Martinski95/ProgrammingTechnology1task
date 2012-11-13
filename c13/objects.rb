class Objects
	def method
		puts "Something in method"
	end
	
	attr_accessor :var
	
	def var=(v)
		@var = v
	end
	
	def var
		@var ||= "asdasfasfasf"
	end
	
	private 
	def method_private
		puts "private"
	end
end


o = Objects.new
o.send :method
o.send :method_private
p o.var
o.var = 10
p o.var