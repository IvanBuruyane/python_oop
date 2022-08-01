import pytest
from Track import TrackLine, Track


@pytest.fixture
def prepare_tracks(equal):
    if equal == "not equal" or equal == "track1 greater":
        track1, track1_point2, track1_point3 = Track(0, 0), TrackLine(2, 4, 100), TrackLine(5, -4, 100)
        track2, track2_point2, track2_point3 = Track(0, 1), TrackLine(3, 2, 90), TrackLine(10, 8, 90)
    elif equal == equal:
        track1, track1_point2, track1_point3 = Track(0, 0), TrackLine(2, 4, 100), TrackLine(5, -4, 100)
        track2, track2_point2, track2_point3 = Track(10, 10), TrackLine(12, 14, 90), TrackLine(15, 6, 90)
    track1.add_track(track1_point2)
    track1.add_track(track1_point3)
    track2.add_track(track2_point2)
    track2.add_track(track2_point3)
    return track1, track2


@pytest.mark.parametrize("equal", ["not equal"])
def test_tracks_not_equal(prepare_tracks):
    track1, track2 = prepare_tracks
    assert len(track1) != len(track2), f"{len(track1), len(track2)}"


@pytest.mark.parametrize("equal", ["equal"])
def test_tracks_equal(prepare_tracks):
    track1, track2 = prepare_tracks
    assert len(track1) == len(track2), f"{len(track1), len(track2)}"


@pytest.mark.parametrize("equal", ["track1 greater"])
def test_tracks_greater(prepare_tracks):
    track1, track2 = prepare_tracks
    assert len(track1) > len(track2), f"{len(track1), len(track2)}"



