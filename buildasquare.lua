--https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/solutions/lua
function generate_shape(n)
   local return_str = ""
   for i=1, n*n do
      return_str = return_str .. "+"
      if i%n == 0 and not (i == n*n) then
	 return_str = return_str .. "\n"
      end
   end
   return return_str
end


print(generate_shape(3))
