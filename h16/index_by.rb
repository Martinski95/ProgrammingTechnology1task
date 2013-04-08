class Array
    def index_by &block
        hash = {}
        self.each do |element|
            temp = yield element
            hash[temp] = element
        end
        hash
    end
end