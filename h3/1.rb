require 'csv'

def process_file_lang
	result_pyth = 0
	result_ruby = 0
	CSV.foreach("test2.csv") do |row|
		if(row[6] == "Python") 
			result_pyth = result_pyth + Integer(row[2])
		elsif(row[6] == "Ruby")
			result_ruby = result_ruby + Integer(row[2])
		end
	end
	printf "Sum using Ruby : %d\n", result_ruby
	printf "Sum using Python : %d\n", result_pyth
	inp = gets
end

process_file_lang