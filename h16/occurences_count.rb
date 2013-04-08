class Array
    def occurences_count
        hash = Hash.new()
        self.each do |element|
            if hash[element] == nil
                hash[element] = 0
            else
                hash[element] += 1
            end
        end
        hash
    end 
end