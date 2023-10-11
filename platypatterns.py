from PIL import Image, ImageDraw
import random


def generate(
    machines,
    tape_width,
    num_colours,
    off_colour=(228, 221, 213),
    on_colour=(0, 0, 0),
    show_machine_states=False,
    max_steps=1600,
    random_rules=False,
    output_filename="output.bmp",
    random_tape=False,
    random_start_positions=False
):

    # Create a blank image
    image_width = tape_width
    image_height = max_steps
    image = Image.new("RGB", (image_width, image_height), (0,30,255))
    draw = ImageDraw.Draw(image)

    machine_index = 0
    turn = 0
    game_over = False

    # if random, set up machines, etc.
    m = 0
    for machine in machines:
        if random_rules:
            machine["name"] = f"m{m}"
            machine["rules"] = [
                [random.randint(0, 1),
                 random.randint(0, 3),
                 random.choice([-1, 1])]
                for _ in range(7)
            ]

        if random_start_positions:
            machine["position"] = random.randint(0, tape_width - 1)
        else:
            machine["position"] = tape_width // 2

        m += 1

    if random_tape:
        board_state = [random.randint(0, 1) for _ in range(tape_width)]
    else:
        board_state = [0] * tape_width

    # MAIN GAME LOOP

    while not game_over:
        machine = machines[machine_index]

        read = board_state[machine["position"]]

        rule_index = machine["state"] * num_colours + read   # find matching rule

        if rule_index >= len(machine["rules"]):
            # print("Machine " + str(machine_index) + " terminated!")
            break

        if turn > max_steps:
            # print("Max turns exceeded!")
            break

        rule = machine["rules"][rule_index]
        board_state[machine["position"]] = rule[0]      # update the current cell based on machine rule
        machine["state"] = rule[1]                      # update machine state
        machine["position"] += rule[2]                  # update machine position

        if machine["position"] >= tape_width:
            machine["position"] = 0
        if machine["position"] < 0:
            machine["position"] = tape_width - 1

        for i, cell in enumerate(board_state):
            x = i
            y = turn
            color = on_colour if cell == 1 else off_colour
            draw.point([x, y], fill=color)

        if show_machine_states:
            draw.point([machine["position"], turn], fill=machine["color"])

        machine_index = (machine_index + 1) % len(machines)
        turn += 1

    # Crop the image to the actual game length
    image = image.crop((0, 0, image_width, turn))

    image.save('run_imgs/' + output_filename, compress_level=0)

    # Return the image filename reference
    return (machines, board_state)


def random_run(run_id,
               num_machines,
               tape_width,
               random_tape,
               random_start_positions,
               max_steps=2048,
               off_colour=(228, 221, 213),
               on_colour=(0, 0, 0),
               ):
    machines = [{
        "id": None,
        "state": 0,
        "position": None,
        "rules": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        "color": None
    }] * num_machines

    (machines, board_state) = generate(machines, tape_width, 2, on_colour, off_colour,
                        False, max_steps, True, output_filename=f"{run_id}.png",
                        random_tape=random_tape, random_start_positions=random_start_positions)

    return (machines, board_state)


# Example usage:
if __name__ == "__main__":
    MACHINES = [
        # Define your machine configurations here
        {
            "id": "m1",
            "state": 0,
            "position": 10,
            "rules": [
                [0, 1, -1],
                [1, 3,  1],
                [1, 2,  1],
                [0, 3,  1],
                [1, 2,  1],
                [0, 2,  1],
                [1, 1,  1],
            ],
            "color": (0, 255, 0)
        },
        {
            "id": "m2",
            "state": 0,
            "position": 30,
            "rules": [
                [0, 2,  1],
                [0, 0, -1],
                [1, 2,  1],
                [0, 2, -1],
                [1, 0,  1],
                [0, 0, -1],
                [0, 3,  1],
            ],
            "color": (255, 255, 255)
        },
        {
            "id": "m3",
            "state": 0,
            "position": 50,
            "rules": [
                [0, 2,  1],
                [0, 2,  1],
                [1, 3,  1],
                [1, 2,  1],
                [1, 2, -1],
                [1, 2,  1],
                [0, 3,  1],
            ],
            "color": (255, 255, 255)
        }
    ]

    generate(
        machines=MACHINES,
        tape_width=101,
        num_colours=2,
        show_machine_states=False,
        max_steps=16000,
        random_rules=False,
        output_filename="output.png",
        random_tape=False,
        random_start_positions=False
    )
