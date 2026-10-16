
class Observation:
    def __init__(self, target, observer, filter_name, exposure):
        self.target = target
        self.observer = observer
        self.filter = filter_name
        self.exposure = exposure
        self.db_id = None

    def summary_info(self):
        return (
            f"target: {self.target}\n"
            f"filter name: {self.filter}\n"
            f"exposure: {self.exposure}\n"
            f"Observer name: {self.observer}"
        )

    def exposure_min(self):
        return self.exposure / 60

    def save_to_db(self, cursor, conn):
        cursor.execute(
            """INSERT INTO observations
            (target, observer, filter_name, exposure)
            VALUES (?, ?, ?, ?)""",
            (
                self.target,
                self.observer,
                self.filter,
                self.exposure
            )
        )
        conn.commit()


class Photometric_observation(Observation):
    def __init__(self, target, observer, filter_name, exposure, wavelength):
        super().__init__(target, observer, filter_name, exposure)
        self.wavelength = wavelength

    def summary_info(self):
        return (
            f"target: {self.target}\n"
            f"filter name: {self.filter}\n"
            f"exposure: {self.exposure}\n"
            f"Observer name: {self.observer}\n"
            f"wavelength: {self.wavelength}"
        )
