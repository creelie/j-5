"""Illustration for the paper (not used in any proof): two pairs of opposite jets
on spheres of radii r > s, and the directions created by their first collisions."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
r, s, gamma = 1.0, 0.62, 1.0

def sphere(ax, R, color):
    u, v = np.mgrid[0:2*np.pi:60j, 0:np.pi:30j]
    ax.plot_surface(R*np.cos(u)*np.sin(v), R*np.sin(u)*np.sin(v), R*np.cos(v),
                    color=color, alpha=0.10, linewidth=0, shade=True)
    ax.plot_wireframe(R*np.cos(u)*np.sin(v), R*np.sin(u)*np.sin(v), R*np.cos(v),
                      color=color, alpha=0.12, rstride=5, cstride=5, linewidth=0.4)

def directions(n):
    x = rng.normal(size=(n, 3))
    return x/np.linalg.norm(x, axis=1)[:, None]

fig = plt.figure(figsize=(9.0, 4.6), dpi=200)
for i, (R, c, lab) in enumerate([(r, "tab:red", "r"), (s, "tab:blue", "s")]):
    ax = fig.add_subplot(1, 2, i+1, projection="3d")
    sphere(ax, R, c)
    n = int(320*(R**gamma))
    p = R*directions(n)
    ax.scatter(p[:, 0], p[:, 1], p[:, 2], s=4, color=c, alpha=0.85, depthshade=False)
    for sg in (1, -1):
        ax.scatter([0], [0], [sg*R], s=70, color=c, edgecolor="k", depthshade=False)
        ax.quiver(0, 0, sg*(R+0.6), 0, 0, -sg*0.5, color="k", arrow_length_ratio=0.25, linewidth=1.4)
    ax.text(0.12, 0, R+0.55, "$+%se$" % lab, color="k", fontsize=12)
    ax.text(0.12, 0, -R-0.75, "$-%se$" % lab, color="k", fontsize=12)
    lim = 1.15
    ax.set_box_aspect((1, 1, 1.25))
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-1.6, 1.6)
    ax.set_axis_off()
    ax.view_init(elev=14, azim=35)
plt.tight_layout()
plt.savefig("fig_jets.png", bbox_inches="tight", pad_inches=0.05)
