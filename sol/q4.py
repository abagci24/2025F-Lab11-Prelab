class TabFileValidationError(Exception):
    pass

def validate_tab_file(file_path, expected_fields, required_pattern):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Check each line for correct number of fields
            for line_num, line in enumerate(lines, start=1):
                # Remove trailing newline and split by tab
                fields = line.rstrip('\n').split('\t')
                
                # Check if number of fields matches expected
                if len(fields) != expected_fields:
                    raise TabFileValidationError(
                        f"File path: {file_path}, Line {line_num}: Expected {expected_fields} fields, found {len(fields)}."
                    )
            
            # Check if at least one field contains the required pattern
            pattern_found = False
            for line in lines:
                fields = line.rstrip('\n').split('\t')
                for field in fields:
                    if required_pattern in field:
                        pattern_found = True
                        break
                if pattern_found:
                    break
            
            if not pattern_found:
                raise TabFileValidationError(
                    f"File path: {file_path}, No field contains required pattern '{required_pattern}'."
                )
        
        return "Tab-delimited file validation passed."
    
    except FileNotFoundError:
        return "File not found."

