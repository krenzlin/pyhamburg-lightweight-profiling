# adapted from: https://www.nylas.com/blog/performance/
import collections
import signal


class Sampler:
    def __init__(self, interval=0.001):
        self.stack_counts = collections.defaultdict(int)
        self.interval = interval
        

    def _sample(self, signum, frame):
        stack = []
        while frame is not None:
            formatted_frame = '{}({})'.format(frame.f_code.co_name,
                                              frame.f_globals.get('__name__'))
            stack.append(formatted_frame)
            frame = frame.f_back

        formatted_stack = ';'.join(reversed(stack))
        self.stack_counts[formatted_stack] += 1


    def start(self):
        signal.signal(signal.SIGVTALRM, self._sample)
        signal.setitimer(signal.ITIMER_VIRTUAL, self.interval, self.interval)


    def stop(self):
        """Call to avoid VIRTUAL TIMER EXPIRED error."""
        signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)


    def save(self, filename):
        with open(filename, 'w') as f:
            for frame, count in self.stack_counts.items():
                f.write('{} {}\n'.format(frame, count))
