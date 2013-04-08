class Array
    def subarray_count subArr
        arrCount = 0
        if subArr.get
            self.each_index do |x|
            if self[x] == subArr[0] && self[x+1] == subArr[1]
                arrCount += 1
            end
        end
        arrCount
    end
end