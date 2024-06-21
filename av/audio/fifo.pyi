from .format import AudioFormat
from .frame import AudioFrame
from .layout import AudioLayout

class AudioFifo:
    def write(self, frame: AudioFrame) -> None: ...
    def read(self, samples: int = 0, partial: bool = False) -> AudioFrame | None: ...
    def read_many(self, samples: int, partial: bool = False) -> list[AudioFrame]: ...
    @property
    def format(self) -> AudioFormat: ...
    @property
    def layout(self) -> AudioLayout: ...
    @property
    def sample_rate(self) -> int: ...
    @property
    def samples(self) -> int: ...