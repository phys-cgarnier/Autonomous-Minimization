import asyncio
def write_record(record):
    # Calculate square of input value
    record.val = record.a * record.a
    print(f"Input: {record.a}, Squared: {record.val}")
