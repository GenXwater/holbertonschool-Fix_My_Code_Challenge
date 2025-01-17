###
# Sort integer arguments (ascending order)
###

sorted_numbers = [] # Array to store sorted integers

# Iterate through each argument provided
ARGV.each do |arg|
  # Skip the argument if it is not a valid integer
  next unless arg.match?(/^[-+]?\d+$/)

  # Convert the argument to an integer
  int_value = arg.to_i

  # Insert the integer into the sorted array at the correct position
  inserted = false
  sorted_numbers.each_with_index do |num, index|
    if int_value < num
      sorted_numbers.insert(index, int_value)
      inserted = true
      break
    end
  end

  # Append the number at the end if not already inserted
  sorted_numbers << int_value unless inserted
end

# Print the sorted array
puts sorted_numbers
