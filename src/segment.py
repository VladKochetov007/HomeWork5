class Segment:
    def __init__(self, start=0, end=0, left_included=True, right_included=True):
        if start > end:
            self.empty = True
            self.start = 0
            self.end = 0
            self.left_included = True
            self.right_included = True
        else:
            self.empty = False
            self.start = start
            self.end = end
            self.left_included = left_included
            self.right_included = right_included
    
    def __str__(self):
        if self.empty:
            return "∅"
        
        left_bracket = "[" if self.left_included else "("
        right_bracket = "]" if self.right_included else ")"
        
        return f"{left_bracket}{self.start}, {self.end}{right_bracket}"
    
    def __repr__(self):
        return self.__str__()
    
    def contains(self, value):
        if self.empty:
            return False
        
        if value < self.start or value > self.end:
            return False
        
        if value == self.start and not self.left_included:
            return False
        
        if value == self.end and not self.right_included:
            return False
        
        return True
    
    def intersects(self, other):
        if self.empty or other.empty:
            return False
        
        if self.end < other.start or self.start > other.end:
            return False
        
        if self.end == other.start:
            return self.right_included and other.left_included
        
        if self.start == other.end:
            return self.left_included and other.right_included
        
        return True


class SegmentSet:
    def __init__(self, segments=None):
        self.segments = []
        
        if segments is not None:
            if isinstance(segments, SegmentSet):
                for segment in segments.segments:
                    self.segments.append(Segment(segment.start, segment.end, 
                                               segment.left_included, segment.right_included))
            elif isinstance(segments, Segment):
                if not segments.empty:
                    self.segments.append(Segment(segments.start, segments.end, 
                                               segments.left_included, segments.right_included))
            elif isinstance(segments, (int, float)):
                self.segments.append(Segment(segments, segments))
            else:
                for segment in segments:
                    if isinstance(segment, Segment) and not segment.empty:
                        self.segments.append(Segment(segment.start, segment.end, 
                                                   segment.left_included, segment.right_included))
        
        self._simplify()
    
    def _simplify(self):
        if not self.segments:
            return
        
        self.segments.sort(key=lambda s: (s.start, not s.left_included))
        
        i = 0
        while i < len(self.segments) - 1:
            current = self.segments[i]
            next_segment = self.segments[i + 1]
            
            if current.end > next_segment.start or (current.end == next_segment.start and 
                                                  (current.right_included or next_segment.left_included)):
                new_end = max(current.end, next_segment.end)
                new_right_included = next_segment.right_included if new_end == next_segment.end else current.right_included
                
                current.end = new_end
                current.right_included = new_right_included
                
                self.segments.pop(i + 1)
            else:
                i += 1
    
    def __str__(self):
        if not self.segments:
            return "∅"
        return " ∪ ".join(str(segment) for segment in self.segments)
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        result = SegmentSet(self.segments)
        
        if isinstance(other, SegmentSet):
            for segment in other.segments:
                result.segments.append(Segment(segment.start, segment.end, 
                                             segment.left_included, segment.right_included))
        elif isinstance(other, Segment):
            if not other.empty:
                result.segments.append(Segment(other.start, other.end, 
                                             other.left_included, other.right_included))
        elif isinstance(other, (int, float)):
            result.segments.append(Segment(other, other))
        
        result._simplify()
        return result
    
    def __mul__(self, other):
        result = SegmentSet()
        
        other_segments = []
        if isinstance(other, SegmentSet):
            other_segments = other.segments
        elif isinstance(other, Segment):
            if not other.empty:
                other_segments = [other]
        elif isinstance(other, (int, float)):
            other_segments = [Segment(other, other)]
        
        for s1 in self.segments:
            for s2 in other_segments:
                if not s1.intersects(s2):
                    continue
                
                start = max(s1.start, s2.start)
                end = min(s1.end, s2.end)
                
                left_included = s1.left_included and s2.left_included if start == s1.start == s2.start else \
                              s1.left_included if start == s1.start else s2.left_included
                
                right_included = s1.right_included and s2.right_included if end == s1.end == s2.end else \
                               s1.right_included if end == s1.end else s2.right_included
                
                intersection = Segment(start, end, left_included, right_included)
                if not intersection.empty:
                    result.segments.append(intersection)
        
        result._simplify()
        return result
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = SegmentSet(Segment(other, other))
        elif isinstance(other, Segment):
            other = SegmentSet(other)
        
        result = SegmentSet()
        
        for segment in self.segments:
            remaining = [segment]
            
            for other_segment in other.segments:
                new_remaining = []
                
                for rem in remaining:
                    if not rem.intersects(other_segment):
                        new_remaining.append(rem)
                        continue
                    
                    if other_segment.start <= rem.start and other_segment.end >= rem.end:
                        if (other_segment.start < rem.start or (other_segment.start == rem.start and other_segment.left_included)) and \
                           (other_segment.end > rem.end or (other_segment.end == rem.end and other_segment.right_included)):
                            continue
                    
                    if rem.start < other_segment.start:
                        left_seg = Segment(rem.start, other_segment.start, rem.left_included, not other_segment.left_included)
                        if not left_seg.empty:
                            new_remaining.append(left_seg)
                    
                    if rem.end > other_segment.end:
                        right_seg = Segment(other_segment.end, rem.end, not other_segment.right_included, rem.right_included)
                        if not right_seg.empty:
                            new_remaining.append(right_seg)
                
                remaining = new_remaining
            
            for rem in remaining:
                result.segments.append(rem)
        
        result._simplify()
        return result
    
    def __truediv__(self, other):
        return (self - other) + (other - self)
    
    def contains(self, value):
        for segment in self.segments:
            if segment.contains(value):
                return True
        return False 