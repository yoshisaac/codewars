fn bool_to_word(b:bool) -> String {
    if b == true {
	return "Yes".to_string()
    } else if b == false {
	return "No".to_string()
    } else {
	return "".to_string()
    }
}

fn main() {
    println!("{}", bool_to_word(false));
}
