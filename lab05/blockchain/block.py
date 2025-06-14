import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        """
        Khởi tạo một khối mới trong blockchain.
        
        Args:
            index (int): Chỉ số của khối.
            previous_hash (str): Hash của khối trước.
            timestamp (float): Thời gian tạo khối.
            transactions (list): Danh sách giao dịch trong khối.
            proof (int): Bằng chứng công việc (proof of work).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Tính toán hash của khối dựa trên các thuộc tính.
        
        Returns:
            str: Hash của khối dưới dạng hex.
        """
        data = (str(self.index) + str(self.previous_hash) + 
                str(self.timestamp) + str(self.transactions) + str(self.proof))
        return hashlib.sha256(data.encode()).hexdigest()